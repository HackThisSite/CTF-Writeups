import sys

def count_combs(left, i, comb, add, denominations):
    if add: comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append( (left, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur), denominations) for x in range(0, int(left/cur)+1))

def main():
    if len(sys.argv) < 3:
        print "Not enough values"
        print "Usage: python2 coin.py amount unit(s)"
        sys.exit(0)

    amount = float(sys.argv[1])
    cents = amount * 100

    combinations = [int(item) for item in sys.argv[2:]]
    print count_combs(cents, 0, [], None, combinations)

if __name__ == "__main__":
    main()
