from string import ascii_uppercase as v, ascii_lowercase as k
def check_flag(s):
        """ Length of the flag should be exactly 25 characters"""
	if len(s) != 0x19:
		return False
	s = list(s)
        """ 0x61a83 => 40003
        lst = [s.pop(r) for r in [20, 17, 15, 13, 11, 2]]
        revlst = lst[::-1]
        strlst = repr(lst)[::-1]
        chars = strlst[2::5] => '400003'
        final = int(chars) = 400003

        From 'lst' we can determine characters position in the flag
        21st character = 3
        18th character = 0
        16th character = 0
        14th character = 0
        12th character = 0
        3rd character = 4

        len(s) = 25 - 6 = 19
        """
	if int(`[s.pop(r) for r in ([2] + [i for i in range(11, 18, 2)] + [20])[::-1]][::-1]`[2::5]) != 0x61a83:
		return False

        """
        ("1"*5)[:2] = "11"
        ("1"*5)[2:] = "111"
        
        The map() statement can be translated as:
        newlst = [int(p, 2) for item in ["11", "111"]]
            where 2 is base i.e. it is converting binary to decimal which gives
            us newlst = [3, 7]

        plist = [s.pop(r) for r in newlst[::-1]]

        Presence of set() tells us that plist might contain same two items.
        We need to keep that in mind.

        list() converts the set(plist) to list again and len() calculates the
        length of this new list.

        Since we have popped two items and used set(), len() might return 1 or 2.
        Let's test for 2.

        If len() returns 2 then it means that "h" is in 3rd position in our
        flag "s" and character at 4th position and 8th position for s (len(s) = 19)
        are different.

        But this is not possible as we have already established that 3rd
        position has '3'.

        Now, we are sure that if len() returns 1 and in 2nd position of our
        flag s, there is a character "h" and characters at 4th position and
        8th position for s (len(s) = 19) have same character.

        len(s) = 19 - 2 = 17
        """
	if len(list(set([s.pop(r) for r in map(lambda p: int(p, 2), [("1"*5)[:2], ("1"*5)[2:]])[::-1]]))) != s.index("h"):
		return False
	y, z = [], []

        """

        rplist = [repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]
        
        y will have len(s) - 1 and len(s) - 3 items of s (len(s) = 17)
        z will have len(s) - 2 and len(s) - 4 items of s
        
        But since list.append() doesn't return anything (None to be precise),
        we will have:
        rplist = ["NoneNone", "NoneNone"]
        set(rplist) => set(['NoneNone'])
        list(set(rplist)) => ['NoneNone']

        len(set(rplist)) will return 1

        len(set(rplist)) - 1 => 0

        Hence, u = 0

        len(s) = 17 - 4 = 13
        """
	u = len(list(set([repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]))) - 1

        """
        Due to the presence of set(), we assume that there are duplicate values
        in 'y' and 'z' for the sake of simplicity.

        ^ means XOR in Python

        Since y and z have two values that are duplicates:

        len(list(set(y))) => 1
        len(list(set(z))) => 1
        
        len(s) = 13
        """
	if u != len(list(set(y))) ^ len(list(set(z))):
		return False
        """
        0x1e = 30
        So, ord(y[0]) ^ ord(z[0]) must be equal to 30. We should keep this in
        mind while choosing characters for our flag.

        len(s) = 13
        """
	if (ord(y[u]) ^ ord(z[u])) ^ 0x1e != 0:
		return False
        """
        v contains all the uppercase letters
        Upto now len(s) = 13

        But s.pop() decreases the length of s by one so len(s) = 12

        We don't know what v.index() returns but we can say that
        len(s) ^ 30 = v.index(s.pop())
        v.index(s.pop()) = 18

        We have 'S' in 19th place so, for s with length = 13 we have 'S' in the end.

        len(s) = 12
        """
	if v.index(s.pop()) ^ len(s) ^ 0x1e != 0:
		return False

        """
        filter(lambda c: c in v, s) returns all the characters that are 
        uppercased in 's'

        Similarly, filter(lambda c: c in k, s) returns all the characters that
        are lowercased in 's' here.

        len(s) = 12 
        """
	a, i = filter(lambda c: c in v, s), filter(lambda c: c in k, s)

        """
        len(s) = 12

        0x50 = 80
        0x4f = 79
        map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 gives us
        [87, 82, 84, 72, 79, 79, 79, 79]

        If we convert each integer from the result to characters, we see that
        it results to ['W', 'R', 'T', 'H', 'O', 'O', 'O', 'O']

        Therefore, a = WRTHOOOOO

        So, we must have WRTHOOOOO within s when len(s) = 12
        """
	if map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 != map(ord, a):
		return False

        """
        i must have these characters: 'a', 'e', 'h' and 't' len(i) = 4

        i[1:3] slices the string and returns 2nd and 3rd character
        
        i[2:0:-1] slices the string from 3rd character to 1st character but not
        including it.

        What we can notice is, first and last character don't change.
        From list("hate") we can say the first character is 'h' and last
        character is 'e'. Since final string should result to "hate" and we
        know that swapping of 2nd and 3rd character happens as
        i[1:3] = i[2:0:-1], we can say that i = "htae"

        We, now, have to fit "htae" within s for len(s) = 12 along with
        "WRTHOOOO"
        """
	i[1:3] = i[2:0:-1]
	if i != list("hate"):
		return False
	return True
