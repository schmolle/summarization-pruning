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

counter_bart = 0
counter_long = 0
counter_pegasus = 0

arr_new_words_bart = []
arr_new_words_long = []
arr_new_words_pegasus = []
max_id_bart = ''
max_value_bart = 0
max_id_long = ''
max_value_long = 0
max_id_pegasus = ''
max_value_pegasus = 0


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
        
        for word in pegasus:
            if word not in base:
                new_words_pegasus = new_words_pegasus + 1
        if new_words_pegasus > 0:
            counter_pegasus = counter_pegasus + 1
        arr_new_words_pegasus.append(new_words_pegasus)
        if new_words_pegasus > max_value_pegasus:
            max_id_pegasus = line_pegasus['id']
            max_value_pegasus = new_words_pegasus     
            
        for word in bart:
            if word not in base:
                new_words_bart = new_words_bart + 1  
        if new_words_bart > 0:
            counter_bart = counter_bart + 1
        arr_new_words_bart.append(new_words_bart)
        if new_words_bart > max_value_bart:
            max_id_bart = line_bart['id']
            max_value_bart = new_words_bart 
                
        for word in long:
            if word not in base:
                new_words_long = new_words_long + 1  
        if new_words_long > 0:
            counter_long = counter_long + 1
        arr_new_words_long.append(new_words_long)
        if new_words_long > max_value_long:
            max_id_long = line_long['id']
            max_value_long = new_words_long 
    
    
    print("counter_bart", counter_bart/full_len)
    print("counter_pegasus", counter_pegasus/full_len)
    print("counter_long", counter_long/full_len)
    overview(arr_new_words_bart, "bart")
    print("%d new in doc %s bart" % (max_value_bart ,max_id_bart))
    overview(arr_new_words_pegasus, "pegasus")
    print("%d new in doc %s pegasus" % (max_value_pegasus ,max_id_pegasus))
    overview(arr_new_words_long, "long")
    print("%d new in doc %s long" % (max_value_long ,max_id_long))