import jsonlines
import os

BASE_PATH = r'/home/jschmolzi/anserini/collections/qrels'
long = os.path.join(BASE_PATH, 'longformer10_qrels_base.json')
bart = os.path.join(BASE_PATH, 'bart10_qrels_base.json')
pegasus = os.path.join(BASE_PATH, 'Pegasus10_qrels_base.json')
base = os.path.join(BASE_PATH, '10_relevant.json')

with jsonlines.open(base, 'r') as f_base, \
        jsonlines.open(bart, 'r') as f_bart,  \
        jsonlines.open(pegasus, 'r') as f_pegasus, \
        jsonlines.open(long, 'r') as f_long:
    for line_base, line_bart, line_pegasus, line_long in zip(f_base, f_bart, f_pegasus, f_long):
        print(line_base['id'])
        print(line_bart['id'])
        print(line_pegasus['id'])
        print(line_long['id'])
        break
        
    
    