import sys
import argparse
import textwrap

__author__ = 'Subhadeep Banerjee'
__version__ = '0.1'

if sys.platform == 'linux':
	from crontab import CronTab
else:
	print(f"Cannot Import Contab in {sys.platform}")

mycron = CronTab(user='matrix')

def takeInput():
	cmd = input("Enter your command:- ")
	time = input("Enter your time in hr:min Format:- ")
	comment = input("Enter the comment:- ")
	return cmd, time, comment

def make(cmd, time, com):
	hr, min = time.split(':')[0], time.split(':')[1]
	job = mycron.new(
		command = cmd,
		comment=com
	)
	job.setall(min, hr, '*', '*', '*')
	mycron.write()
	print("New CronJob Made.")


def update(cmd, time, com):
	for job in mycron:
		if job.comment == com:
			hr, min = time.split(':')[0], time.split(':')[1]
			job = mycron.new(
				command = cmd,
				comment=com
			)
			job.setall(min, hr, '*', '*', '*')
			mycron.write()
	print("Existing Cron Job Updated.")
			

def remove(com=None):
	if com != None:
		for job in mycron:
			if job.comment == com:
				mycron.remove(job)
				print("Cront Deleted")
				mycron.write()
			print(f"Job deleted with comment {com}")
	else:
		print("Without Comment cannot remove.")


def show():
	for job in mycron:
		print(job)

def removeAll():
	mycron.remove_all()
	mycron.write()
	print("All Cron Job Deleted.")

def main():
	parser = argparse.ArgumentParser(prog='app.py',
                                     usage="%(prog)a [OPTIONS] python3 pycron.py -m -s",
                                     description=textwrap.dedent('''
                                     This is a auto cronjob setup tool, in python.
                                     '''),
                                     add_help=True,
                                     allow_abbrev=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter
                                     )
	subparser = parser.add_subparsers()

	parser.add_argument('-m',
                        '--make',
						action='store_true',
                        help='To make a new cronjob.'
                        )
	parser.add_argument('-u',
                        '--update',
						action='store_true',
                        help='To update and exsisting cronjob.'
						)
	parser.add_argument('-r',
                        '--remove',
						type=str,
                        help="Remove an existing cronjob."
						)
	parser.add_argument('-ra',
                        '--removeAll',
						action='store_true',
                        help="Removes all existing cronjobs."
						)
	parser.add_argument('-s',
                        '--show',
						action='store_true',
                        help="Show all the cronjob."
						)
	args =  parser.parse_args()

	if args.make:
		cmd, time, comment = takeInput()
		make(cmd, time, comment)
	elif args.update:
		cmd, time, comment = takeInput()
		update(cmd, time, comment)
	elif args.remove:
		remove(args.remove)
	elif args.removeAll:
		removeAll()
	elif args.show:
		show()
	else:
		parser.print_help()

if __name__ == '__main__':
	main()