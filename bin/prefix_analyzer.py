from summarize import Longformer_Impl_With_Pipeline
import logging
import os
import sys
from transformers import LEDTokenizer
from datasets import load_dataset
import time

	
def filter_by_token_length(input, tokenizer):
	max_tokens = 16384
	min_tokens = 300
	txt = input['contents']
	tokens = tokenizer(txt, return_tensors="pt").input_ids[0]
	token_length = len(tokens)
	return (token_length <= max_tokens) and (token_length >= min_tokens)

def check_prefix(input, idx, pipeline):
	if idx % 1000 == 0:
		logging.info("%d summarized" % (idx,))
	summarized_array = []
	
	new_contents = pipeline.summarize(input['contents'], 50, 30)
	summarized_array[0] = new_contents[0]['summary_text'].split('\n')[0]
	
	new_contents = pipeline.summarize(input['contents'], 100, 80)
	summarized_array[1] = new_contents[0]['summary_text'].split('\n')[0]
	
	new_contents = pipeline.summarize(input['contents'], 150, 170)
	summarized_array[2] = new_contents[0]['summary_text'].split('\n')[0]
	if summarized_array[1].startswith(summarized_array[0]) and summarized_array[2].startswith(summarized_array[0]) and summarized_array[2].startswith(summarized_array[1]):
		input["is_prefix"] = True
	return True
	
def sum_file(infile_path, outfile_path, device):
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline(device)
	longformer_tokenizer = LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv")
	
	dataset = load_dataset('json', data_files=infile_path)	
	dataset = dataset['train']
	
	logging.info("Filtering...")
	dataset = dataset.filter(lambda input: filter_by_token_length(input, longformer_tokenizer), num_proc=30)
	dataset = dataset.shuffle(seed=42).select(range(20000))
	
	new_column = [False] * len(dataset)
	dataset = dataset.add_column("is_prefix", new_column)
	logging.info("DONE!!!")
			
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
		
		try:
			sum_file(infile_path, outfile_path, device)
		except Exception as e:
			logging.error(e)		
		
	# logging.info('Run Finished')