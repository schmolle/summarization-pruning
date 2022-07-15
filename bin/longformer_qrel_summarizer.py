from summarize import Longformer_Impl_With_Pipeline
from summarize import Bart_Impl_With_Pipeline
from summarize import Pegasus_Impl_With_Pipeline
import logging
import os
import sys
from transformers import LEDTokenizer
from datasets import load_dataset


def map_to_summary(input, idx, pipeline):
	max_tokens = 16384
	token_length = min(max_tokens, input['token_length'])
	sumarize_length = token_length // 2
	if idx % 1000 == 0:
		logging.info("%d summarized" % (idx,))
	new_contents = pipeline.summarize(input['contents'], max_length=sumarize_length, min_length=sumarize_length)
	input['contents'] = new_contents[0]['summary_text']
	return input
	
def add_token_length(input, tokenizer):
	txt = input['contents']
	tokens = tokenizer(txt, return_tensors="pt").input_ids[0]
	token_length = len(tokens)
	input['token_length'] = token_length
	return input
	
def sum_file(infile_path, outfile_path, device):
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline(device)
	longformer_tokenizer = LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv")
	
	# Loading dataset
	dataset = load_dataset('json', data_files=infile_path)	
	dataset = dataset['train']
	
	# adding column for token length
	new_column = [0] * len(dataset)
	dataset = dataset.add_column("token_length", new_column)
	
	logging.info("Counting Tokens...")
	dataset = dataset.map(lambda input: add_token_length(input, longformer_tokenizer), num_proc=30)
	
	logging.info("Summarizing...")
	dataset = dataset.map(lambda input, idx: map_to_summary(input, idx, longformer_pipeline), with_indices=True)
	
	logging.info("Storing...")
	dataset.to_json(outfile_path)
	logging.info("DONE!!!")
			
if __name__ == "__main__":
	logging.info('Run Started')
	infile_path = '/home/jschmolzi/anserini/collections/qrels/relevant.json'
	outfile_path = '/home/jschmolzi/anserini/collections/qrels/longformer_qrels_base.json'
	logfile = '/home/jschmolzi/logs/longformer.log'
	device = 0
	
	if os.path.isfile(logfile):
		os.remove(logfile)		
	logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)
	print(f'Logging to file {logfile}')
	print(f'Writing to file {outfile_path}')
	
	try:
		sum_file(infile_path, outfile_path, device)
	except Exception as e:
		logging.error(e)		
		
	# logging.info('Run Finished')