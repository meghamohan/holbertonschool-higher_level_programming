#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    if(len(sys.argv) != 4):
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    if (op != '+' or op != '-' or op != '*' or op != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if (op == '+'):
        res = add(int(sys.argv[1]), int(sys.argv[3]))
    if (op == '-'):
        res = sub(int(sys.argv[1]), int(sys.argv[3]))
    if (op == '*'):
        res = mul(int(sys.argv[1]), int(sys.argv[3]))
    if (op == '/'):
        res = div(int(sys.argv[1]), int(sys.argv[3]))
    print("{} {} {} = {}".format(sys.argv[1], op, sys.argv[3], res))

    if(__name__ == "__main__"):
        main()
