import sys

if sys.platform == 'linux':
	from crontab import Crontab
else:
	raise ImportError(f"Cannot Import Contab in {sys.platform}")
