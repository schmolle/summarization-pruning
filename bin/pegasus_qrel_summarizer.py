from summarize import Pegasus_Impl_With_Pipeline
import logging
import os
import sys
from transformers import PegasusTokenizer
from datasets import load_dataset


def map_to_summary(input, idx, pipeline):
	max_tokens = 512
	token_length = min(max_tokens, input['token_length'])
	sumarize_length = token_length // 2
	sumarize_length = min(512, sumarize_length)
	if idx % 1000 == 0:
		logging.info("%d summarized" % (idx,))
	try:
		if sumarize_length > 5:
			new_contents = pipeline.summarize(input['contents'], sumarize_length, sumarize_length)
			input['contents'] = new_contents[0]['summary_text']
		else:
			logging.info('token_length: %s' % (token_length,))
			logging.info('contents: %s' % (input['contents'],))
			logging.info('id: %s' % (input['id'],))
	except Exception as e:
		logging.error(e)
		logging.info('token_length: %s' % (token_length,))
		logging.info('contents: %s' % (input['contents'],))
		logging.info('id: %s' % (input['id'],))
		raise e	
	return input
	
def add_token_length(input, tokenizer):
	txt = input['contents']
	tokens = tokenizer(txt, return_tensors="pt").input_ids[0]
	token_length = len(tokens)
	input['token_length'] = token_length
	return input
	
def sum_file(infile_path, outfile_path, device):
	longformer_pipeline = Pegasus_Impl_With_Pipeline.PegasusWithPipeline(device)
	longformer_tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
	
	# Loading dataset
	dataset = load_dataset('json', data_files=infile_path)	
	dataset = dataset['train']
	
	# adding column for token length
	new_column = [0] * len(dataset)
	dataset = dataset.add_column("token_length", new_column)
	
	logging.info("Counting Tokens...")
	dataset = dataset.map(lambda input: add_token_length(input, longformer_tokenizer))
	
	logging.info("Summarizing...")
	dataset = dataset.map(lambda input, idx: map_to_summary(input, idx, longformer_pipeline), with_indices=True)
	
	logging.info("Storing...")
	dataset.to_json(outfile_path)
	logging.info("DONE!!!")
			
if __name__ == "__main__":

	infile_path = '/home/jschmolzi/anserini/collections/qrels/relevant.json'
	outfile_path = '/home/jschmolzi/anserini/collections/qrels/Pegasus_qrels_base.json'
	logfile = '/home/jschmolzi/logs/Pegasus.log'
	device = 1
	
	if os.path.isfile(logfile):
		with open(logfile, 'w') as f:
			pass
	logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)
	print(f'Logging to file {logfile}')
	print(f'Writing to file {outfile_path}')
	
	logging.info('Run Started')
	try:
		sum_file(infile_path, outfile_path, device)
	except Exception as e:
		logging.error(e)		
		
	# logging.info('Run Finished')