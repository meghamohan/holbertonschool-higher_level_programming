#!/usr/bin/python3
def main():
    import sys
    sum = 0
    for i in sys.argv[1:]:
        sum += int(i)
    print("{:d}".format(sum))
if(__name__ == "__main__"):
    main()
