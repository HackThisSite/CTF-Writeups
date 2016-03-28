import argparse
import math

# Our methods
def lroot(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Please check the value of 'a' and 'c'")
    x = (-b - math.sqrt(delta))/(2*1.0*a)
    return int(x)

def groot(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Please check the value of 'a' and 'c'")
    x = (-b + math.sqrt(delta))/(2*1.0*a)
    return int(x)

def main():
    # Initialize a parser
    parser = argparse.ArgumentParser(description="Finds greater or lesser root of" +
            "quadratic equations of the form: ax^2 + bx + c = 0")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-g", "--greater", action="store_true", help="Find Greater root")
    group.add_argument("-l", "--lesser", action="store_true", help="Find Lesser root")
    parser.add_argument("a", type=int, help="Value of 'a' in ax^2 + bx + c")
    parser.add_argument("b", type=int, help="Value of 'b' in ax^2 + bx + c")
    parser.add_argument("c", type=int, help="Value of 'c' in ax^2 + bx + c")
    args = parser.parse_args()

    gr,lr = args.greater,args.lesser
    a,b,c = args.a,args.b,args.c

    if args.greater:
        try:
            print groot(a, b, c)
        except Exception as e:
            print e
    else:
        try:
            print lroot(a, b, c)
        except Exception as e:
            print e

if __name__ == "__main__":
    main()
