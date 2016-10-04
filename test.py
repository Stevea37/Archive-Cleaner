from Calculator import *
import sys


def main():
    calc = Calculator(sys.argv[1], sys.argv[2:])
    results = calc.calculate()
    for i in results:
        print(i)

if __name__ == '__main__':
    main()


