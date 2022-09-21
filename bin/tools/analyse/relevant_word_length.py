import jsonlines
import os
import numpy as np

BASE_PATH = r'/home/jschmolzi/anserini/collections/qrels'

long = os.path.join(BASE_PATH, 'longformer10_qrels_base.json')
bart = os.path.join(BASE_PATH, 'bart10_qrels_base.json')
pegasus = os.path.join(BASE_PATH, 'Pegasus10_qrels_base.json')
base = os.path.join(BASE_PATH, '10_relevant.json')

arr_len_bart = []
arr_len_long = []
arr_len_pegasus = []

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

with jsonlines.open(bart, 'r') as f_bart,  \
        jsonlines.open(pegasus, 'r') as f_pegasus, \
        jsonlines.open(long, 'r') as f_long:
    
    for line_bart, line_pegasus, line_long in zip(f_bart, f_pegasus, f_long):     
        bart = line_bart['contents'].split()
        pegasus = line_pegasus['contents'].split()
        long = line_long['contents'].split()
        
        arr_len_bart.append[len(bart)]
        arr_len_pegasus.append[len(pegasus)]
        arr_len_long.append[len(long)]
    
    
    print("counter_bart", len(arr_len_bart))
    print("counter_pegasus", len(arr_len_pegasus))
    print("counter_long", len(arr_len_long))
    
    overview(arr_len_bart, "bart")
    overview(arr_len_pegasus, "pegasus")
    overview(arr_len_long, "long")
    