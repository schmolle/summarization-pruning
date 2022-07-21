from qrel_defs import qrel_file_path

def filter_top100_qrels(inpath):
    qrels = set()
    with open(inpath, 'r') as infil:
        for line in infile:
            line_array = line.split(' ')
            dok_id = line_array[2]
            dok_rank = line_array[3]
            set.add(dok_id)
            break

if __name__ == "__main__":
    inpath = '/home/jschmolzi/data/msmarco-docdev-top100'
    filter_top100_qrels(inpath)