import jsonlines
import os
import re
import numpy as np

def overview(arr, name):
    min = np.min(arr)
    max = np.max(arr)
    mean = np.mean(arr)
    avg = np.average(arr)
    print("overview %s" % (name,))
    print("\tmin: %s" % (min,))
    print("\tmax: %s" % (max,))
    print("\tmean: %s" % (mean,))
    print("\tavg: %s" % (avg,))
    
    
BASE_PATH = r'/home/jschmolzi/anserini/collections/qrels'
full_len = 51465
long = os.path.join(BASE_PATH, 'longformer10_qrels_base.json')
bart = os.path.join(BASE_PATH, 'bart10_qrels_base.json')
pegasus = os.path.join(BASE_PATH, 'Pegasus10_qrels_base.json')
base = os.path.join(BASE_PATH, '10_relevant.json')

filter_regex = '[^a-zA-Z0-9 \n]'

arr_new_words_bart = []
arr_new_words_long = []
arr_new_words_pegasus = []

arr_missing_words_bart = []
arr_missing_words_long = []
arr_missing_words_pegasus = []

with jsonlines.open(base, 'r') as f_base, \
        jsonlines.open(bart, 'r') as f_bart,  \
        jsonlines.open(pegasus, 'r') as f_pegasus, \
        jsonlines.open(long, 'r') as f_long:
    for line_base, line_bart, line_pegasus, line_long in zip(f_base, f_bart, f_pegasus, f_long):
        new_words_bart = 0
        new_words_long = 0
        new_words_pegasus = 0
        
        base = line_base['contents']
        base = re.sub(filter_regex, '', base)
        base = base.split()
        
        bart = line_bart['contents']
        bart = re.sub(filter_regex, '', bart)
        bart = bart.split()
        
        pegasus = line_pegasus['contents']
        pegasus = re.sub(filter_regex, '', pegasus)
        pegasus = pegasus.split()
        
        
        long = line_long['contents']
        long = re.sub(filter_regex, '', long)
        long = long.split()
        
        base_length = len(base)
        bart_length = len(bart)
        pegasus_length = len(pegasus)
        long_length = len(long)
        
        if base_length < 50:       
        
            bart_counter = 0
            pegasus_counter = 0
            long_counter = 0
            
            for word in base:
                if word not in bart:
                    bart_counter = bart_counter + 1
                arr_missing_words_bart.append(bart_counter)
                
                if word not in pegasus:
                    pegasus_counter = pegasus_counter + 1
                arr_missing_words_pegasus.append(pegasus_counter)
                
                if word not in long:
                    long_counter = long_counter + 1
                arr_missing_words_long.append(long_counter)
            if (bart_counter > 0 or pegasus_counter > 0 or long_counter > 0):
                print("doc_id %s: bart %d, pega %d, long %d ----- full %d" % (line_base['id'], bart_counter, pegasus_counter, long_counter, base_length))