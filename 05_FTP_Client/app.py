import os
import sys
import ftplib
import argparse
import textwrap


class FTPTest:
    def __init__(self, host: str, user: str = None, password: str = None) -> None:
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        if self.host and self.user and self.password:
            try:
                ftp = ftplib.FTP(self.host, self.user, self.password)
            except ftplib.error_perm as e:
                ftp = None
                error_code = str(e).split(None, 1)
                if error_code[0] == '530':
                    ftp = ftplib.FTP(self.host)
        ftp.login()
        resp = ftp.getwelcome()
        print(f'loging Response {resp}')
        return ftp

    @staticmethod
    def allowed_commands() -> None:
        print("""
                ALLOWED COMMANDS-----------------------------------------------------------------
                |   1.  PWD          -       (Print Working Directory)                          |
                |   2.  DIR          -       (Directory Listing)                                |
                |   3.  LIST         -       (Retrieves List of Files and Information)          |
                |   4.  NLST         -       (Retrieves a list of file names)                   |
                |   5.  CD DirName   -       (Change Directory)                                 |
                |   6.  DFS FileName -       (Download File For Server, and sets a default name)|
                |   7.  UFS FileName -       (Upload File to Server)                            |
                |   8.  RM FileName  -       (Rename a File in Server)                          |
                |   9.  DEL FileName -       (Delete a File from the Server)                    |
                |   10. MKD DirName  -       (Make a directory in Server)                       |
                |   11. RMD DirName  -       (Remove a Directory in Server)                     |
                |   12. SZI FileName -       (Get the Size of the File from the Server)         |
                |   13. QUIT         -       (Close the Connection to the Server)               |
                ---------------------------------------------------------------------------------
                """)

    def operations(self) -> None:
        ftp = self.connect()
        while True:
            self.allowed_commands()
            command = input('Enter a Command :- ')
            commands = command.split()
            if commands[0] == 'PWD':  # 1
                print(ftp.pwd())
            elif commands[0] == 'DIR':  # 2
                ftp.dir()
            elif commands[0] == 'LIST':  # 3
                ftp.retrlines('LIST')
            elif commands[0] == 'NLST':  # 4
                ftp.retrlines('NLST')
            elif commands[0] == 'CD':  # 5
                print(f"The Current Wroking Directory is - {ftp.pwd()}")
                ftp.cwd(commands[1])
                print(f"The Current Wroking Directory is - {ftp.pwd()}")
            elif commands[0] == 'DFS':  # 6
                print(commands[1])
                try:
                    with open(commands[1], 'wb') as fp:
                        ftp.retrbinary(f'RETR {commands[1]}', fp.write)
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'File May Not Exist or You May Not Have Permission To Download it.')
                else:
                    print(f"Downloaded Status - Completed")
            elif commands[0] == 'UFS':  # 7
                try:
                    with open(commands[1], 'rb') as fp:
                        ftp.storbinary(f'STOR {commands[1]}', fp.read)
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'File May Not Exist or You May Not Have Permission To Upload it.')
                else:
                    print(f"Upload Status - Completed")
                    print(ftp.nlst())
            elif commands[0] == 'RM':  # 8
                try:
                    new_name = input("Enter a New Name for the File")
                    ftp.rename(commands[1], new_name)
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'File May Not Exist or You May Not Have Permission To Rename it.')
                else:
                    print("Sucessfully Renamed File!")
                    print(ftp.nlst())
            elif commands[0] == 'DEL':  # 9
                try:
                    ftp.delete(commands[1])
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'File May Not Exist or You May Not Have Permission To Delete it.')
                else:
                    print("Sucessfully Deleted File!")
                    print(ftp.nlst())
            elif commands[0] == 'MKD':  # 10
                try:
                    ftp.mkd(commands[1])
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'You Do Not Have Permission to Make Directory in the Server!')
                else:
                    print("Sucessfully Created Directory!")
                    print(ftp.nlst())
            elif commands[0] == 'RMD':  # 11
                try:
                    ftp.rmd(commands[1])
                except ftplib.error_perm as e:
                    error_code = str(e).split(None, 1)
                    if error_code[0] == '550':
                        print(
                            error_code[1], 'You Do Not Have Permission to Delete Directory in the Server!')
                else:
                    print("Sucessfully Removed Directory!")
                    print(ftp.nlst())
            elif commands[0] == 'SZI':  # 12
                size = ftp.size(commands[1])
                print(f"Size Of The Requested File Is - {size}")
            elif commands[0] == 'QUIT':  # 13
                try:
                    print(ftp.quit())
                except ftplib.all_errors():
                    print(ftp.close())
                finally:
                    break
            else:
                print("Enter a Valid Option!!")


# Helper Function
def main():
    parser = argparse.ArgumentParser(prog='app.py',
                                     usage='%(prog)a [OPTIONS] -H ftp.us.debian.org -U matrix -P xxxxx',
                                     description=textwrap.dedent(''' 
                                                    FTP CLIENT
                                     This Program is capable of Performing all the 
                                     operations Like a Usual FTP Client does.'''),
                                     add_help=True,
                                     allow_abbrev=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-H',
                        '--host',
                        type=str,
                        help='Use it to Specify Host')
    parser.add_argument('-U',
                        '--user',
                        type=str,
                        help='Use it to Specify Username')
    parser.add_argument('-P',
                        '--passwd',
                        type=str,
                        help='Use it to Specify Password')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error - {e}")
    if args.host and args.user and args.passwd:
        HOST = args.host
        USERNAME = args.user
        PASSWORD = args.passwd
        return (HOST, USERNAME, PASSWORD)
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        host, user, passwd = main()
        ftp = FTPTest(host, user, passwd)
        ftp.operations()
    except TypeError:
        sys.exit(1)
