from Crypto.Cipher import AES
import hash
import struct

#Xor previous state, with the current 10 char block.
def xor_block(state, block):
  block += '\x00'*6
  result = ""
  for i in range(16):
    result += chr(ord(state[i]) ^ ord(block[i]))
  return result

#Getting our AES instance
ZERO_AES = AES.new('\x00'*16)

# Pad the input string
GIVEN_STRING = 'I love using sponges for crypto'

def getTarget():
    #ADD FINAL INGEST CHARS, AND CALL IT PADDED
    EXTRA = len(GIVEN_STRING) % 10
    if EXTRA == 9:
      PADDED = GIVEN_STRING + '\x81'
    else:
      PADDED = GIVEN_STRING + '\x80' + '\x00'*(8-EXTRA) + '\x01'
    assert(len(PADDED) % 10 == 0)
    BLOCKS = len(PADDED) // 10

    #GET FINAL STATE BEFORE SQUEEZE
    # Find the target state
    TARGET = '\x00'*16
    for i in range(BLOCKS):
      TARGET = xor_block(TARGET, PADDED[10*i:10*(i+1)])
      TARGET = ZERO_AES.encrypt(TARGET)

    # Sanity check: does squeezing this state yield the right result?
    TMP = TARGET
    RESULT = ""
    for i in range(2):
      RESULT += TMP[:10]
      TMP = ZERO_AES.encrypt(TMP)
    assert(RESULT == hash.Hasher().hash(GIVEN_STRING))

    # Go backwards through the part that's the same every time
    # UNDO FINAL AES
    TARGET = ZERO_AES.decrypt(TARGET)
    # GO BACK ONE STATE
    TARGET = xor_block(TARGET, '\x80' + '\x00'*8 + '\x01')
    # COMPLETE GOING BACK ONE STATE. We are now at the third block being about to be AES'd
    TARGET = ZERO_AES.decrypt(TARGET)
    return TARGET

TARGET = getTarget()
# Now we meet in the middle!
#
# Our collision string is going to be exactly 3 blocks long.  We try random 1st
# and 3rd blocks until we get one where the intermediate states agree after
# the first 10 bytes.  Then the 2nd block is just the xor of the two
# intermediate states.

def try_reverse(block):
  return ZERO_AES.decrypt(xor_block(TARGET, block))

def try_forwards(block):
  return ZERO_AES.encrypt(block + '\x00'*6)

def collide():
  FORWARD_MAP = {}
  REVERSE_MAP = {}
  i = 0
  upperbound = 2**80
  while(i < upperbound):
    block = struct.pack("<I", i)
    if(len(block) < 10):
      block = block + '\x00'*(10-len(block))
    forwards = try_forwards(block)[10:]
    reverse = try_reverse(block)[10:]
    FORWARD_MAP[forwards] = block
    REVERSE_MAP[reverse] = block
    if forwards in REVERSE_MAP:
      return block, REVERSE_MAP[forwards]
    if reverse in FORWARD_MAP:
      return FORWARD_MAP[reverse], block
    i += 1
    if i % 200000 == 0:
      print "i =", i

def interpolate(first, third):
  forwards = try_forwards(first)
  reverse = try_reverse(third)
  second = ""
  for i in range(10):
    second += chr(ord(forwards[i]) ^ ord(reverse[i]))
  for i in range(10, 16):
    assert(forwards[i] == reverse[i])
  return second

# Let's do this.
first, third = collide()
second = interpolate(first, third)
print len(first + second + third)
print first + second + third
print (first+second+third).encode('hex')
print hash.Hasher().hash(first+second+third) == hash.Hasher().hash(GIVEN_STRING)
