import sys
from transformers import LEDTokenizer
from datasets import load_dataset

def extract_lengths():
    infile_path = '/home/jschmolzi/anserini/collections/qrels/relevant.json'
    dataset = load_dataset('json', data_files=infile_path)    
    dataset = dataset['train']
    print(dataset['contents'])
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'e':
            extract_lengths() 