import sys
from datasets import load_dataset
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt


def extract_lengths(tokenizer, tokenizer_id):
    infile_path = '/home/jschmolzi/anserini/collections/qrels/10_relevant.json'
    outfile_base_path = '/home/jschmolzi/data'
    dataset = load_dataset('json', data_files=infile_path)    
    dataset = dataset['train']
    contents = dataset['contents']
    content_lengths = []
    
    for content in contents:
        tokens = tokenizer(content, return_tensors="pt").input_ids[0]
        token_length = len(tokens)
        content_lengths.append(token_length)
    outfile_path = os.path.join(outfile_base_path, tokenizer_id)
    with open(outfile_path, 'w+b') as outfile:
        pickle.dump(content_lengths, outfile)
        
def clear_long_entries(in_arr, max):
        in_arr = [np.min([max, x]) for x in in_arr]
        return in_arr
    
def get_number_of_occurences(in_arr, value):
    counter = 0
    for x in in_arr:
        if x == value:
            counter = counter + 1
    return counter

def create_overview(model_name):
    print("Creating %s overview" % (model_name,))
    with open(os.path.join('/home/jschmolzi/data', model_name), 'rb') as infile:
            arr = pickle.load(infile)
            min = np.min(arr)
            max = np.max(arr)
            mean = np.mean(arr)
            avg = np.average(arr)

            print("min: %s" % (min,))
            print("max: %s" % (max,))
            print("mean: %s" % (mean,))
            print("avg: %s" % (avg,))
            
            arr = clear_long_entries(arr, 20000)
            
            min = np.min(arr)
            max = np.max(arr)
            mean = np.mean(arr)
            avg = np.average(arr)
            longer_20000 = get_number_of_occurences(arr, 20000)
            
            plt.hist(arr, bins='auto');
            plt.title('%s tokens of %d relevant Docs' % (model_name, len(arr)))
            plt.xlabel('Tokens')
            
            plt.savefig('/home/jschmolzi/summarization-pruning/data/plots/%s_plot.png' % (model_name,))
            print("min: %s" % (min,))
            print("max: %s" % (max,))
            print("mean: %s" % (mean,))
            print("avg: %s" % (avg,))
            print("longer_20000: %s" % (longer_20000,))
            plt.clf()
            
            
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '1':
            from transformers import LEDTokenizer
            extract_lengths(LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv"), 'longformer')
        elif sys.argv[1] == '2':
            from transformers import BartTokenizer
            extract_lengths(BartTokenizer.from_pretrained("facebook/bart-large-cnn"), 'bart')
        elif sys.argv[1] == '3':
            from transformers import PegasusTokenizer
            extract_lengths(PegasusTokenizer.from_pretrained("google/pegasus-xsum"), 'pegasus')
        else:
            print("Usage: 1=longformer, 2=bart, 3=pegasus")
    else:
        create_overview('bart')
        create_overview('pegasus')
        create_overview('longformer')
