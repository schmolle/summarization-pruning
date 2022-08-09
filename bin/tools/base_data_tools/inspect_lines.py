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

	with gzip.open('/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz','rt') as f:
		for line in f:
			print(line)
			counter = counter + 1
			if counter > 100:
				break

	logging.info("ended run")
except Exception as e:
	logging.error(e)

