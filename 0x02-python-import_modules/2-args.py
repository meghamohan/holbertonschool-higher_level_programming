#!/usr/bin/python3
def main():
    import sys
    if(len(sys.argv) == 1):
        print("0 argument.")
    elif(len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    n = 1
    for i in sys.argv[1:]:
        print("{:d}: {}".format(n, i))
        n = n + 1
if(__name__ == "__main__"):
    main()
