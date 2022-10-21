import jsonlines
import os
import re
import numpy as np
import sys
   
    
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

id = sys.argv[1]
print(id)
with jsonlines.open(base, 'r') as f_base, \
        jsonlines.open(bart, 'r') as f_bart,  \
        jsonlines.open(pegasus, 'r') as f_pegasus, \
        jsonlines.open(long, 'r') as f_long:
    for line_base, line_bart, line_pegasus, line_long in zip(f_base, f_bart, f_pegasus, f_long):
        new_words_bart = 0
        new_words_long = 0
        new_words_pegasus = 0
        
        line_id = line_base['id']
         
        if id == line_id:
            base = line_base['contents']
            pegasusbase_len = len(base.split()) 
    
            bart = line_bart['contents']
            bart_len = len(bart.split())
    
            pegasus = line_pegasus['contents']
            pegasus_len = len(pegasus.split())
            
            long = line_long['contents']
            long_len = len(long.split())
            
            print("base: ")
            print(base)
            print(base_len)
            print("bart: ")
            print(bart)
            print(bart_len)
            print("pegasus: ")
            print(pegasus)
            print(pegasus_len)
            print("long: ")
            print(long)
            print(long_len)
            

