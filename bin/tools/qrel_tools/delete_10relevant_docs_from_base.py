from qrel_defs import qrel_json_file_path
from read_10qrels import read_qrels
import os
import jsonlines
import json


if __name__ == '__main__':
    indir = '/home/jschmolzi/anserini/collections/base'
    qrel_arr = read_qrels()
    counter = 0
    for infile_path in os.listdir(indir):
        if infile_path != 'relevant.json':
            infile_path = os.path.join(indir, infile_path)
            outfile_path = infile_path
            with jsonlines.open(infile_path, 'r') as infile:
                json_list = [line for line in infile]
            with open(infile_path, 'w') as outfile:
                for line in json_list:
                    id = line['id']                
                    if id in qrel_arr:
                        counter = counter + 1
                        if counter % 200 == 0:
                            print("%d relevant docs found" % (counter,))
                    else:
                        outfile.write(json.dumps(line) + '\n')
    print("%d relevant docs found" % (counter,))
    
    