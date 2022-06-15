from summarize import Longformer_Impl_With_Pipeline
import logging
import os
import json
import jsonlines

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
			
			if counter > 5:
				break
			if (counter % 10000) == 0:
				logger.info("%d items queued" % (counter,))
			counter = counter + 1
			
def consumer(q, outfile_name, longformer):
	with open(outfile_name, 'w+') as outfile:
		while true:
			item = queue.get()
	        if item is None:
	            queue.put(item)
	            break
	        try:
	        	new_contents = longformer.summarize(line['contents'])
	        	line['contents'] = new_contents[0]['summary_text']
	        	outfile.write(json.dumps(line) + '\n')
	        except Exception as e:
				logger.error("Failed to Process line: id: %s, url:%s, title: %s, contents: %s" % (line['id'], line['url'], line['title'], line['contents']))
				logger.error("With error %s" % (e,))
		

if __name__ == "__main__":
	# logging.info('Run Started')
	print(f'Logging to file {logfile}')
	infile_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00.json'
	outdir_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-00'
	filename = infile_name.split('/')[-1]
	outfile_name_0 = os.path.join(outdir_name, '0', filename)
	outfile_name_1 = os.path.join(outdir_name, '1', filename)
	print(f'Writing to file {outfile_name_0}')
	print(f'Writing to file {outfile_name_1}')
	
	longformer_pipeline_device_0 = Longformer_Impl_With_Pipeline.LongformerWithPipeline(0)
	longformer_pipeline_device_1 = Longformer_Impl_With_Pipeline.LongformerWithPipeline(1)
	
	q = queue.Queue(30)
	
	consumers = [Thread(target=consumer, args=(q, outfile_name_0, longformer_pipeline_device_0)),
				 Thread(target=consumer, args=(q, outfile_name_1, longformer_pipeline_device_1))]
	
	for consumer in consumers:
		consumer.start()
		
	producer = Thread(target=producer, args=(q, infile_name))
	producer.start()
	producer.join()
	
	for consumer in consumers:
		consumer.join()	
	# logging.info('Run Finished')