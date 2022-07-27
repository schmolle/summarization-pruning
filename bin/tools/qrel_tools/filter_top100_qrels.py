from qrel_defs import qrel_file_path
from read_qrels import read_qrels

def filter_top100_qrels(inpath):
    top10_qrels = set()
    top1_qrels = set()
    counter = 0
    counter2 = 0
    with open(inpath, 'r') as infile:
        for line in infile:
            line_array = line.split(' ')
            dok_rank = line_array[3]
            dok_rank = int(dok_rank)
            if dok_rank <= 10:
                counter2 = counter2 + 1
                dok_id = line_array[2]
                top10_qrels.add(dok_id)
                if dok_rank == 1:
                    top1_qrels.add(dok_id)
                    counter = counter + 1
    print("top1  qrels: %s" % (len(top1_qrels),))           
    print("top10 qrels: %s" % (len(top10_qrels),))
    print(counter)
    print(counter2)
    old_qrels = read_qrels()
    old_qrels = set(old_qrels)
    all = top10_qrels.intersection(old_qrels)
    print(len(all))
    
    
if __name__ == "__main__":
    inpath = '/home/jschmolzi/data/msmarco-docdev-top100'
    filter_top100_qrels(inpath)