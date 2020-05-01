#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    count = len(args)

    if count == 3:

        a = int(args[0])
        b = int(args[2])

        if args[1] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif args[1] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif args[1] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        elif args[1] == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
