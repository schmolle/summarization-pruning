import gzip
import logging
from datetime import datetime

logging.basicConfig(filename='inspect.log', level=logging.DEBUG)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
logging.info("started run at: %s\n" % (current_time,))
try:
	logg
	counter = 3213835
	max_length = 0
	min_length = 0
	longer1024 = 0

	with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
		for line in f:
			length = len(line)
			if length < min_length: min_length = length
			if length > max_length: max_length = length
			if length > 1024: longer1024 = longer1024 + 1

	logging.info("TOTAL LINES %s" % (counter,))
	logging.info("longer1024 %s" % (longer1024,))
	logging.info("min_length %s" % (min_length,))
	logging.info("max_length %s" % (max_length,))

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	logging.info("started run at: %s\n" % (current_time,))
except Exception as e:
	logging.error(e)
