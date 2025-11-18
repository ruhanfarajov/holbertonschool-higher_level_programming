#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, div, mul


def calc(a, op, b):
    result = 1
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    return result


def main(lst):
    operands = ["+", "-", "*", "/"]
    if len(lst) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif lst[1] not in operands:
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        answer = calc(int(lst[0]),  lst[1], int(lst[2]))
        print("{} {} {} = {}".format(lst[0],  lst[1],  lst[2], answer))


lst = argv[1:]

if __name__ == "__main__":
    main(lst)
