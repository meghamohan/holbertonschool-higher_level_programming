#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) != 4):
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if (op == '+'):
        res = add(a, b)
    if (op == '-'):
        res = sub(a, b)
    if (op == '*'):
        res = mul(a, b)
    if (op == '/'):
        res = div(a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, res))

if(__name__ == "__main__"):
    main()
