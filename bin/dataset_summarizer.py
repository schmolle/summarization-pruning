from summarize import Longformer_Impl_With_Pipeline
import logging
import os
import sys
from transformers import LEDTokenizer
from datasets import load_dataset


def map_to_summary(input, idx, pipeline):
	if idx % 10000 == 0:
		logger.info("%d indexed" % (idx,))
	new_contents = pipeline.summarize(input['contents'])
	input['contents'] = new_contents[0]['summary_text']
	return input
	
def filter_by_token_length(input, tokenizer):
	max_tokens = 16384
	txt = input['contents']
	tokens = tokenizer(txt, return_tensors="pt").input_ids[0]
	token_length = len(tokens)
	return token_length <= max_tokens
	
def sum_file(infile_path, outfile_path, device):
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline(device)
	longformer_tokenizer = LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv")
	print("Models loaded")
	
	dataset = load_dataset('json', data_files=infile_path)	
	dataset = dataset['train'].select(range(100))
	
	logger.info("Filtering...")
	dataset = dataset.filter(lambda input: filter_by_token_length(input, longformer_tokenizer))
	dataset = dataset.select(range(10))
	
	logger.info("Summarizing...")
	dataset = dataset.map(lambda input, idx: map_to_summary(input, idx, longformer_pipeline), with_indices=True)
	
	logger.info("Storing...")
	dataset.to_json(outfile_path)
	logger.info("DONE!!!")
			
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
		if os.path.isfile(logfile):
			os.remove(logfile)
			
		logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)
		print(f'Logging to file {logfile}')
		
		filename = infile_path.split('/')[-1]
		outfile_path = os.path.join(outfile_path, filename)
		print(f'Writing to file {outfile_path}')
		
		sum_file(infile_path, outfile_path, device)
				
		
	# logging.info('Run Finished')