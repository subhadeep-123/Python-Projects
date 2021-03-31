import os
import sys
import shutil


def main(orgFile, newName):
    path = os.path.split(orgFile)[0]
    a = shutil.copyfile(orgFile, os.path.join(path, newName))
    os.remove(orgFile)
    print("Operation Complete, You may check now.")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
