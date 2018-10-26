#!/usr/bin/env python3


def calculate(arg):

    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            result = val1 + val2

            if (token == '+'):
                result = val1 + val2

            elif (token == '-'):
                result = val1 - val2

            elif (token == '*'):
                result = val1 * val2;

            elif (token == '/'):
                result = val1 / val2


            stack.append(result);
            return stack[0]


def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
