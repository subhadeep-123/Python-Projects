import os
import errno
import logging
import getpass
import shutil
import textwrap
import argparse


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s || %(levelname)s || %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger.setLevel(10)

username = getpass.getuser()


def clearTemp():
    path = 'C:\Windows\Temp'
    tempFiles = os.listdir(path)
    i = 0
    logger.debug(f"Items Available in the Drectory is :- {tempFiles}")
    logger.warning('Starting to Remove Files/Folders.\n')
    while i != len(tempFiles):
        logger.debug(f'Performing Remove operation on {tempFiles[i]}')
        try:
            if os.path.isfile(os.path.join(path, tempFiles[i])) == True:
                os.remove(os.path.join(path, tempFiles[i]))
            else:
                os.rmdir(os.path.join(path, tempFiles[i]))
        except Exception as err:
            if err.errno == errno.EACCES:
                logger.error(os.strerror(errno.EACCES))
            elif err.errno == errno.ETXTBSY:
                logger.error(os.strerror(errno.ETXTBSY))
        else:
            logger.warning(f"Removed - {tempFiles[i]}")
        i += 1
    else:
        logger.debug(
            f"Remainig Items in the Directory are - {os.listdir(path)}")


def clearPercentTemp():
    path = f'C:/Users/{username}/AppData/Local/Temp'
    tempFiles = os.listdir(path)
    i = 0
    logger.debug(f"Items Available in the Drectory is :- {tempFiles}")
    logger.warning('Starting to Remove Files/Folders.\n')
    while i != len(tempFiles):
        logger.debug(f'Performing Remove operation on {tempFiles[i]}')
        try:
            if os.path.isfile(os.path.join(path, tempFiles[i])) == True:
                os.remove(os.path.join(path, tempFiles[i]))
            else:
                try:
                    os.rmdir(os.path.join(path, tempFiles[i]))
                except Exception as err:
                    shutil.rmtree(os.path.join(path, tempFiles[i]))
        except Exception as err:
            if err.errno == errno.EACCES:
                logger.error(os.strerror(errno.EACCES))
            elif err.errno == errno.ETXTBSY:
                logger.error(os.strerror(errno.ETXTBSY))
        else:
            logger.warning(f"Removed - {tempFiles[i]}")
        i += 1
    else:
        logger.debug(
            f"Remainig Items in the Directory are - {os.listdir(path)}")


def clearPrefetch():
    path = 'C:\Windows\Prefetch'
    tempFiles = os.listdir(path)
    i = 0
    logger.debug(f"Items Available in the Drectory is :- {tempFiles}")
    logger.warning('Starting to Remove Files/Folders.\n')
    while i != len(tempFiles):
        logger.debug(f'Performing Remove operation on {tempFiles[i]}')
        try:
            if os.path.isfile(os.path.join(path, tempFiles[i])) == True:
                os.remove(os.path.join(path, tempFiles[i]))
            else:
                try:
                    os.rmdir(os.path.join(path, tempFiles[i]))
                except Exception as err:
                    shutil.rmtree(os.path.join(path, tempFiles[i]))
        except Exception as err:
            if err.errno == errno.EACCES:
                logger.error(os.strerror(errno.EACCES))
            elif err.errno == errno.ETXTBSY:
                logger.error(os.strerror(errno.ETXTBSY))
        else:
            logger.warning(f"Removed - {tempFiles[i]}")
        i += 1
    else:
        logger.debug(
            f"Remainig Items in the Directory are - {os.listdir(path)}")

# Helper Function


def main():
    parser = argparse.ArgumentParser(prog='app.py',
                                     usage='%(prog)a [OPTIONS] --ctemp ||--cptemp || --cprefetch',
                                     description=textwrap.dedent('''
                                     This tool helps us to automates
                                     cache clearing in windows.
                                     '''
                                                                 ),
                                     add_help=True,
                                     allow_abbrev=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('-ct',
                        '--ctemp',
                        help='This is for clearing Temp dir',
                        action="store_true")
    parser.add_argument('-cpt',
                        '--cptemp',
                        help='This is for clearing Local Temp dir',
                        action="store_true")
    parser.add_argument('-cp',
                        '--cprefetch',
                        help='This is for clearing Prefetch directory.',
                        action="store_true")
    parser.add_argument('-a',
                        '--all',
                        help='This is for clearing TempDir, percentTempDir, and Prefetch Dir',
                        action="store_true")

    args = parser.parse_args()
    if args.ctemp:
        clearTemp()
    elif args.cptemp:
        clearPercentTemp()
    elif args.cprefetch:
        clearPrefetch()
    elif args.all:
        clearTemp()
        clearPercentTemp()
        clearPrefetch()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
