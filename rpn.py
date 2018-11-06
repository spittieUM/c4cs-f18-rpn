#!/usr/bin/env python3
import operator


op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
    '%': operator.mod
}


def calculate(arg):

    stack = arg.split()

    while (len(stack) > 1):
        token = stack.pop()

        try:
            value = int(token)
            stack.append(value)

        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            func = op[token]
            result = func(val1, val2)

            stack.append(result);
            print (stack[0])
            return int(stack[0])


def main():
    calcFunc = ''
    while calcFunc != 'q':
        calcFunc = input("rpn calc> ")
        calculate(calcFunc)


if __name__ == '__main__':
    main()
