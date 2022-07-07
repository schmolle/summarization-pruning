import os
from read_qrels import read_qrels

if __name__ == '__main__':
    infile_path = '/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.tsv'
    qrel_arr = read_qrels()
    counter = 0
    with open(infile_path, 'r') as infile:
        for line in infile:
            id, url, title, body = line.split('\t')
            if id in qrel_arr:
                counter = counter + 1
                if counter % 200 == 0:
                    print("%d relevant docs found" % (counter,))
    print("%d relevant docs found" % (counter,))
    
    