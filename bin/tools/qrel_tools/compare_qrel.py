from qrel_defs import qrel10_file_path
from read_10qrels import read_qrels
    
    
def get_qrel_from_id(id):
    path = '/home/jschmolzi/data/qrels/msmarco-docdev-queries.tsv'
    with open(path, 'r') as f:
        for line in f:
            f_split = line.split()
            f_id = int(f_split[0])
            if id == f_id:
                print("%d: %s" % (f_id, ' '.join(f_split[1:])))
    
if __name__ == '__main__':
    relevant_qrels = read_qrels()
    get_qrel_from_id(1101279)
    