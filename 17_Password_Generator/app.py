import copy
import random
import getpass
import logging
import argparse
import textwrap
import datetime

"""
Password Examples
R9_3bJL8*zX&pSC
sMq@Y*C6HrR86fC
"""
__author__ = 'Subhadeep Banerjee'
__version__ = '0.1'

allowdedCharacters = ['@', '%', '+', '/', '!', '#', '&', '*', '_', '$', '?', ]

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s || %(levelname)s || %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def shorten(diff, name=None, sdate=None):
    logger.debug(f"The Recieved Difference is - {diff}")
    if name != None:
        logger.info(f'To Short - {name}')
        return name[:-diff]
    else:
        logger.info(f'To Short - {sdate}')
        sdate = sdate[:-diff]
        logger.info(f"After Shortning - {sdate}")


def mergeSort(name, sdate):
    logger.warning(''.join([name, sdate]))

    # Doing Operation on Name
    name = list(name)
    for i in range(0, len(name)):
        if i % 2 == 0:
            name[i] = name[i].upper()
    else:
        name.sort()

    # Removing the Duplicates from the name, sdate
    newName = removDuplicates(name)
    newSdate = removDuplicates(sdate)

    return newPassword(newName, newSdate)


def removDuplicates(oldobj):
    newList = list()
    for i in oldobj:
        if i not in newList:
            newList.append(i)
    return newList


def newPassword(name, date):
    newPasswd = list()
    copyChars = copy.deepcopy(allowdedCharacters)
    for i in [name, date, copyChars]:
        random.shuffle(i)
        if i == name:
            newPasswd.extend(i[:7])
        elif i == copyChars:
            newPasswd.extend(i[:4])
        else:
            newPasswd.extend(i[:4])
    random.shuffle(newPasswd)
    return ''.join(newPasswd)


def main(name, date):

    sdate = date.split('-')
    sdate.append(str(datetime.datetime.now().time()).split('.')[1])
    sdate = ''.join(sdate)

    logger.warning(f"The join Data and Time is - {sdate}, {len(sdate)}")

    # After Removing the Space and Merging the name
    name = ''.join([i for i in name if i != ' '])
    logger.warning(f"The Entered Name is - {name}, {len(name)}")

    # Checking For Lengt Difference
    diff = len(name) - len(sdate)
    if diff < 0:
        diff = abs(diff)
        logger.debug(f"Name is short by - {diff}")
        logger.debug(f"After Shortning - {shorten(diff, sdate)}")
    elif diff > 0:
        logger.debug(f"Sdate is short by - {diff}")
        logger.debug(f"After Shortning - {shorten(diff, name)}")
    else:
        logger.info("Both Have same length, Need no modification.")

    # Now Merginig
    logger.critical(f"The Generated Password - {mergeSort(name, sdate)}")


if __name__ == '__main__':
    Name = None
    Date = None
    parser = argparse.ArgumentParser(prog='app.py',
                                     usage="%(prog)a [OPTIONS] python app.py -u 'Subhadeep Banerjee' -d '22-07-1999' -vv ",
                                     description=textwrap.dedent('''
                                     This is auto password generator tool.
                                     It can work with or without input
                                     '''),
                                     add_help=True,
                                     allow_abbrev=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('-u',
                        '--name',
                        type=str,
                        help='This is to spicify a name. Takes the OS account username as default if nothing is specified.',
                        default=str(getpass.getuser())
                        )
    parser.add_argument('-d',
                        '--date',
                        type=str,
                        default=str(datetime.datetime.now().date()),
                        help='This is to spicify a date. Takes the current date as default if nothing is specified.')
    parser.add_argument('-v',
                        '--verbose',
                        action='count',
                        default=0,
                        help="each 'v' increases vebosity of logging.")
    args = parser.parse_args()

    if args.verbose <= 3:
        if args.verbose == 1 or args.verbose == 0:
            logger.setLevel(40)
        elif args.verbose == 2:
            logger.setLevel(20)
        elif args.verbose == 3:
            logger.setLevel(10)
        else:
            print("LogLevel Is At Default")

    if args.name and args.date:
        main(args.name, args.date)
    else:
        parser.print_help()
