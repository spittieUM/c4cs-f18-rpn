#!/usr/bin/env python3
import operator


op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculate(arg):

    stack = arg.split()

    while (len(stack) > 1):
        token = stack.pop();

        try:
            value = int(token)
            stack.append(value)

        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()

            func = op[token]
            result = func(val1, val2)

            stack.append(result);
            return stack[0]


def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
