from qrel_defs import qrel_file_path

def filter_top100_qrels(inpath):
    qrels = set()
    with open(inpath, 'r') as infile:
        for line in infile:
            print(line)
            line_array = line.split(' ')
            print(line_array)
            dok_id = line_array[2]
            print(dok_id)
            dok_rank = line_array[3]
            print(dok_rank)
            qrels.add(dok_id)
            break
    print(qrels)
    
if __name__ == "__main__":
    inpath = '/home/jschmolzi/data/msmarco-docdev-top100'
    filter_top100_qrels(inpath)