from qrel_defs import qrel10_file_path
from read_10qrels import read_qrels
import sys
    
def get_qrel_from_id(id):
    path = '/home/jschmolzi/data/qrels/msmarco-docdev-queries.tsv'
    with open(path, 'r') as f:
        for line in f:
            f_split = line.split()
            f_id = f_split[0]
            if id == f_id:
                print("%s: %s" % (f_id, ' '.join(f_split[1:])))

def compare_base_bart(id):
    base_path = r'~/anserini/runs/run.base.txt'
    bart_path = '~/anserini/runs/run.bart.txt'
    for line_base, line_bart in zip(base_path, bart_path):
        base_split = line_base.split()
        base_id = base_split[0]
        base_rank = int(base_split[3])
        base_dokid = base_split[4]
        
        bart_split = line_bart.split()
        bart_id = bart_split[0]
        bart_rank = int(bart_split[3])
        bart_dokid = bart_split[4]
        
        if base_id == id and base_rank < 11:
            print("base %d: %s --- bart %d: %s" % (base_id, base_dokid, bart_id, bart_dokid))
        
        
def get_qrel_info(id):
    get_qrel_from_id(id)
    compare_base_bart(id)
        
        
if __name__ == '__main__':
    relevant_qrels = read_qrels()
    get_qrel_info(sys.argv[1])
    