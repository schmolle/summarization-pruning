from summarize import Longformer_Impl_With_Pipeline
import logging
import os
import sys
import json
import jsonlines

		
def sum_file(infile_path, outfile_path, device):
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline(device)
	print("Model loaded")
	counter = 0
	with jsonlines.open(infile_path, 'r') as infile, open(outfile_path, 'w+') as outfile:
		for line in infile:
			if (counter % 10000) == 0:
				logging.info("%d lines summarized" % (counter,))
			counter = counter + 1
			new_contents = longformer_pipeline.summarize(line['contents'])
			line['contents'] = new_contents[0]['summary_text']
			outfile.write(json.dumps(line) + '\n')
			
			
if __name__ == "__main__":
	# logging.info('Run Started')
	args = sys.argv
	if len(args) != 5:
		print("Usage: infile outfile logfile device")
		# infile_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00aa.json'
		# outfile_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-00'
		# logfile = '/home/jschmolzi/logs/tools/summarizer1.log'
	else:
		infile_path = args[1]
		outfile_path = args[2]
		logfile = args[3]
		device = int(args[4])
		
		logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)
		print(f'Logging to file {logfile}')
		
		filename = infile_path.split('/')[-1]
		outfile_path = os.path.join(outfile_path, filename)
		print(f'Writing to file {outfile_path}')
		
		sum_file(infile_path, outfile_path, device)
		
			
		
	# logging.info('Run Finished')