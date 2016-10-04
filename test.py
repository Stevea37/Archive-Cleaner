from Calculator import *
import sys


def main():
    calc = Calculator(sys.argv[1], sys.argv[2:])
    results = calc.calculate()


if __name__ == '__main__':
    main()


