from qrel_defs import qrel_json_file_path
from read_qrels import read_qrels
import os
import jsonlines
import json


if __name__ == '__main__':
    indir = '/home/jschmolzi/anserini/collections/base'
    relevant_path = 'relevant.json'
    outfile = open(os.opath.join(indir, relevant_path), 'w')
    qrel_arr = read_qrels()
    counter = 0
    for infile_path in os.listdir(indir):
        if infile_path != 'relevant.json':
            infile_path = os.path.join(indir, infile_path)
            with jsonlines.open(infile_path, 'r') as infile:
                for line in infile:
                    id = line['id']
                    if id in qrel_arr:
                        outfile.write(json.dumps(line) + '\n')
                        counter = counter + 1
                        if counter % 200 == 0:
                            print("%d relevant docs found" % (counter,))
    outfile.close()
    print("%d relevant docs found" % (counter,))
    
    