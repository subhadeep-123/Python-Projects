import os
import sys
import errno
import shutil


def main(orgFile, newName):
    path = os.path.split(orgFile)[0]
    try:
        a = shutil.copyfile(orgFile, os.path.join(path, newName))
        os.remove(orgFile)
    except FileNotFoundError as err:
        if err.errno == errno.ENOENT:
            print('\nThe File Does Not Exist.')
    else:
        print("Operation Complete, You may check now.")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
