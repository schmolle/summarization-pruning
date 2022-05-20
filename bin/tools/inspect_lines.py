import gzip
import logging
from datetime import datetime
from transformers import PegasusTokenizerFast

logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/jschmolzi/logs/tools/data.log', level=logging.DEBUG)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
logging.info("############################################################################")
logging.info("started run")
try:
	counter = 0

	with gzip.open('/home/jschmolzi/collections/msmarco-doc/msmarco-docs.trec.gz','rt') as f:
		for line in f:
			length = len(line) 
			if lenght < 20:
				logger.info("Line %d with length %d found" % (counter, length))
			counter = counter + 1

	logging.info("ended run")
except Exception as e:
	logging.error(e)

