import os
import sys
import time
import shutil
import getpass
import logging
import textwrap
import argparse
import requests


logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s || %(levelname)s || %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger.setLevel(10)

username = getpass.getuser()


class DownloadLinkMissionError(Exception):
    pass


def downloadImage(imgLink, path=None):
    logger.info(f"Image Link Recived - {imgLink}")
    filename = imgLink.split('/')[-1]
    logger.info(f'Image File Name - {filename}')
    if path == None:
        if not os.path.exists('Image'):
            os.mkdir('Image')
            logger.info(f'Making Image Folder in current Directory.')
        path = os.path.abspath('Image')
    else:
        logger.info(f'Specified path is - {path}')
    try:
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(imgLink, stream=True)
    except requests.exceptions.MissingSchema as err:
        logger.error(err)
    except Exception as e:
        logger.error(e)
    else:
        if r.status_code == 200:
            logger.info(f"Selected Directory - {os.path.split(path)[1]}")
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # Open a local file with wb ( write binary ) permission.
            with open(os.path.join(path, filename), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
                logger.info(f"Image Downloaded Sucessfuly - {filename}")
        else:
            logger.critical('Image Couldn\'t be retreived')


def main():
    parser = argparse.ArgumentParser(prog='app.py',
                                     usage="%(prog)a [OPTIONS] python app.py -d -l https://img1.10bestmedia.com/Images/Photos/379272/GettyImages-104489865_54_990x660.jpg -dr ",
                                     description=textwrap.dedent('''
                                     This tool is a CLI based Image downloading
                                     tool.
                                     '''),
                                     add_help=True,
                                     allow_abbrev=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
    parser.add_argument('-d',
                        '--download',
                        help='This argument is for activating the download Flasg',
                        action="store_true")
    parser.add_argument('-l',
                        '--link',
                        type=str,
                        help='This argument is for specifying the image link')
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        help='This argument is for specifying the file link')
    parser.add_argument('-dr',
                        '--downloaddir',
                        type=str,
                        help='This argument is for specifying the download directory')

    args = parser.parse_args()
    if args.download:
        if not args.downloaddir:
            path = None
        path = args.downloaddir
        if not args.link and not args.file:
            raise DownloadLinkMissionError(
                'The Download Link/Links is not specified.')
        else:
            if args.link:
                link = args.link
                downloadImage(link, path)
            elif args.file:
                with open(args.file, 'r') as f:
                    links = f.read().split(',')
                    for i in links:
                        downloadImage(i, path)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
