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


def summarize(infile_name, outdir_name):
	filename = infile_name.split('/')[-1]
	outfile_name = os.path.join(outdir_name, filename)
	print(f'Writing to file {outfile_name}')
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline()
	with jsonlines.open(infile_name, 'r') as infile, open(outfile_name, 'w+') as outfile:
		for line in infile:
			print(line['id'])
			print(line['url'])
			print(line['title'])
			print(line['contents'])
			
			new_contents = longformer_pipeline.summarize(txt)(line['contents'])
			line['contents'] = new_contents
			
			print(line['id'])
			print(line['url'])
			print(line['title'])
			print(line['contents'])
			
			outfile_name.write(json.dumps(line) + '\n')
			break		
	

if __name__ == "__main__":
	# logging.info('Run Started')
	infile_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/docs00.json'
	outdir_name = '/home/jschmolzi/anserini/collections/msmarco-doc-json-00'
	summarize(infile_name, outdir_name)
	
	# logging.info('Run Finished')