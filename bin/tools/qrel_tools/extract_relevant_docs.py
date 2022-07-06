from qrel_defs import qrel_json_file_path
from read_qrels import read_qrels
import os


if __name__ == '__main__':
    indir = '/home/jschmolzi/anserini/collections/base'
    for infile_path in os.listdir(indir):
        if infile_path != 'relevant.json':
            print(os.path.join(indir, infile_path))
    # qrel_arr = read_qrels()
    
    