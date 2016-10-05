from Calculator import *
from Cleaner import *
from argparse import RawDescriptionHelpFormatter, RawTextHelpFormatter
import argparse


def main():
    description = "Cleans up old backups to leave more room on the backup server." \
                  "\n\nE.g. python cleaner.py -p /path/to/archive -o 3:4 7:7." \
                  "\n\nThe example provided will keep an archive from every 4th day if it's more than 3 days old" \
                  " and archive every 7 days if it's more than a week old." \
                  "\n\nThe format of backups this script takes is BACKUP_SET-VERSION."
    parser = argparse.ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-p', '--root-path', type=str, required=True, help='The root path of your backups.')
    parser.add_argument('-o', '--options', type=str, required=True, nargs='*',
                        help='Your age threshold and desired interval size separated by a colon')
    parser.add_argument('-f', '--force', action='store_true', help='Automatically confirms that you want to delete.')
    args = parser.parse_args()

    calc = Calculator(args.root_path, args.options, args.force)
    calc.calculate()

    cleaner = Cleaner(calc)
    cleaner.clean()

if __name__ == '__main__':
    main()
