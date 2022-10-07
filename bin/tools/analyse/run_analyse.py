import jsonlines
import os

base_path = r'/home/jschmolzi/anserini/runs/eval/base.txt'
long_path = os.path.join(BASE_PATH, '/home/jschmolzi/anserini/runs/eval/longformer.txt')
bart_path = os.path.join(BASE_PATH, '/home/jschmolzi/anserini/runs/eval/bart.txt')
pegasus_path = os.path.join(BASE_PATH, '/home/jschmolzi/anserini/runs/eval/pegasus.txt')

for f_name in [bart_path, long_path, pegasus_path]:
    counter = 0
    worse_5 = []
    same_5 = []
    better_5 = []
    
    worse_10 = []
    same_10 = []
    better_10 = []    
    print("Datei: %s" % (f_name,))
    with open(base_path, 'r') as f_base, \
            open(f_name, 'r') as f_current:
        for line_base, line_current in zip(f_base, f_current):
            base_split = line_base.split()
            current_split = line_current.split()
            ndcg_base = float(base_split[2])
            ndcg_current = float(current_split[2])
            if (counter % 2) == 0:
                if ndcg_base == ndcg_current:
                    same_5.append(base_split[1])
                if ndcg_base > ndcg_current:
                    worse_5.append(base_split[1])
                if ndcg_base < ndcg_current:
                    better_5.append(base_split[1])
            else:
                if ndcg_base == ndcg_current:
                    same_10.append(base_split[1])
                if ndcg_base > ndcg_current:
                    worse_10.append(base_split[1])
                if ndcg_base < ndcg_current:
                    better_10.append(base_split[1])
            counter = counter + 1
    print("better @5: %d" % (len(better_5)))
    print("same @5: %d" % (len(same_5)))
    print("worse @5: %d" % (len(worse_5)))
    
    print("better @10: %d" % (len(better_10)))
    print("same @10: %d" % (len(same_10)))
    print("worse @10: %d" % (len(worse_10)))
    