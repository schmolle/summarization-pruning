from qrel_defs import qrel_json_file_path
from read_qrels import read_qrels
import os
import jsonlines


if __name__ == '__main__':
    indir = '/home/jschmolzi/anserini/collections/base'
    relevant_path = 'relevant.json'
    outfile = open(relevant_path, 'w')
    qrel_arr = read_qrels()
    for infile_path in os.listdir(indir):
        if infile_path != 'relevant.json':
            infile_path = os.path.join(indir, infile_path)
            with jsonlines.open(infile_path, 'r') as infile:
                for line in infile:
                    id = line['id']
    outfile.close()
    
    