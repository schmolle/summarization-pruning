import jsonlines
import os

BASE_PATH = r'/home/jschmolzi/anserini/collections/qrels'
full_len = 51465
long = os.path.join(BASE_PATH, 'longformer10_qrels_base.json')
bart = os.path.join(BASE_PATH, 'bart10_qrels_base.json')
pegasus = os.path.join(BASE_PATH, 'Pegasus10_qrels_base.json')
base = os.path.join(BASE_PATH, '10_relevant.json')

counter = 0
with jsonlines.open(base, 'r') as f_base, \
        jsonlines.open(bart, 'r') as f_bart,  \
        jsonlines.open(pegasus, 'r') as f_pegasus, \
        jsonlines.open(long, 'r') as f_long:
    for line_base, line_bart, line_pegasus, line_long in zip(f_base, f_bart, f_pegasus, f_long):
        id_base = line_base['id']
        id_bart = line_bart['id']
        id_pegasus = line_pegasus['id']
        id_long = line_long['id']
        
        if id_base == id_bart & id_base == id_pegasus & id_base == id_long:
            counter = counter + 1
        else:
            print("Mistake in line", counter)
    print(counter, "lines are the same")
    