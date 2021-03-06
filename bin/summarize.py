from summarize import Longformer_Impl_With_Pipeline
import logging
import os
import json
import jsonlines
from threading import Thread
from queue import Queue

if os.name == 'nt':
	logfile = "../logs/summarizer.log"
else:
	logfile = '/home/jschmolzi/logs/tools/summarizer.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)

def producer(q, infile_name):
	counter = 0
	with jsonlines.open(infile_name, 'r') as infile:
		for line in infile:
			q.put(line)
			if (counter % 10000) == 0:
				logging.info("%d items queued" % (counter,))
			counter = counter + 1
		q.put(None)
def consumer(q, outfile, longformer):
	while True:
		item = q.get()
		if item is None:
			q.put(item)
			break
		try:
			new_contents = longformer.summarize(item['contents'])
			item['contents'] = new_contents[0]['summary_text']
			outfile.write(json.dumps(item) + '\n')
		except Exception as e:
			logging.error("Failed to Process line: id: %s, url:%s, title: %s, contents: %s" % (item['id'], item['url'], item['title'], item['contents']))
			logging.error("With error %s" % (e,))
		

if __name__ == "__main__":
	# logging.info('Run Started')
	print(f'Logging to file {logfile}')
	infile_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00.json'
	outdir_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-00'
	filename = infile_name.split('/')[-1]
	outfile_name_0 = os.path.join(outdir_name, '0' + filename)
	outfile_name_1 = os.path.join(outdir_name, '1' + filename)
	print(f'Writing to file {outfile_name_0}')
	print(f'Writing to file {outfile_name_1}')
	
	longformer_pipeline_device_0 = Longformer_Impl_With_Pipeline.LongformerWithPipeline(0)
	longformer_pipeline_device_1 = Longformer_Impl_With_Pipeline.LongformerWithPipeline(1)
	print("Models loaded")
	
	q = Queue(30)
	
	with open(outfile_name_0, 'w+') as outfile_0, open(outfile_name_1, 'w+') as outfile_1:
		consumers = [Thread(target=consumer, args=(q, outfile_0, longformer_pipeline_device_0)),
					 Thread(target=consumer, args=(q, outfile_1, longformer_pipeline_device_1))]
		
		for consumer in consumers:
			consumer.start()
			
		producer = Thread(target=producer, args=(q, infile_name))
		producer.start()
		producer.join()
		
		for consumer in consumers:
			consumer.join()	
	# logging.info('Run Finished')