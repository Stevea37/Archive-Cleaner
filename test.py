from Calculator import *
import sys


def main():
    calc = Calculator(sys.argv[1], sys.argv[2:])
    for archive in calc.archives:
        print(os.path.basename(archive))


if __name__ == '__main__':
    main()
