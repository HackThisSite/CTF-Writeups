# pip install secretsharing
# https://github.com/blockstack/secret-sharing
from secretsharing import PlaintextToHexSecretSharer as SS

with open('message1.txt', 'r') as f:
  PLAINTEXTS = [f.read()] * 5

for i in range(2, 6):
  with open('message' + str(i) + '.txt', 'r') as f:
    msg = f.read()
  shares = SS.split_secret(msg, i, 5)
  for j in range(5):
    PLAINTEXTS[j] += shares[j] + '\n'

for j in range(5):
  with open('plaintext-' + str(j+1) + '.txt', 'w') as f:
    f.write(PLAINTEXTS[j])

