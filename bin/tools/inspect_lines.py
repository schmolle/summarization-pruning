import gzip
import logging
from datetime import datetime
from transformers import PegasusTokenizerFast

logging.basicConfig(format='%(asctime)s %(message)s', filename='~/logs/tools/data.log', level=logging.DEBUG)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
logging.info("############################################################################")
logging.info("started run")
try:
	counter = 0

	with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
		for line in f:
			length = len(line) 
			if lenght < 20:
				logger.info("Line %s with length %s found" % (counter, length))
			counter = counter + 1

	logging.info("ended run")
except Exception as e:
	logging.error(e)

