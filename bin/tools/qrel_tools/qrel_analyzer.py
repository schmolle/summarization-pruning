import sys
from datasets import load_dataset
import pickle
import os
from pip._vendor.distlib._backport.tarfile import _FileInFile

def extract_lengths(tokenizer, tokenizer_id):
    infile_path = '/home/jschmolzi/anserini/collections/qrels/10_relevant.json'
    outfile_base_path = '/home/jschmolz/data'
    dataset = load_dataset('json', data_files=infile_path)    
    dataset = dataset['train']
    contents = dataset['contents']
    content_lengths = []
    
    for content in contents:
        tokens = tokenizer(content, return_tensors="pt").input_ids[0]
        token_length = len(tokens)
        content_lengths.append(token_length)
    print(len(content_lengths))
    print(content_lengths[5:20])
    outfile_path = os.path.join(outfile_base_path, tokenizer_id)
    with open(outfile_path, 'w+b') as outfile:
        pickle.dump(content_lengths, outfile)
        
        
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
        with open('/home/jschmolz/data/bart', 'rb') as infile:
            arr = pickle.load(infile)
            print(len(arr))
            print(arr[5:20])