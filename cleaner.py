import sys
from Calculator import *
from Cleaner import *


def main():
    calc = Calculator(sys.argv[1], sys.argv[2:])
    calc.calculate()

    cleaner = Cleaner(calc)
    cleaner.clean()

if __name__ == '__main__':
    main()
