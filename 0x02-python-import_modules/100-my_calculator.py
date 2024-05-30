#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = __import__('calculator_1').add
    sub = __import__('calculator_1').sub
    mul = __import__('calculator_1').mul
    div = __import__('calculator_1').div
    # from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} + {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} + {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} + {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
