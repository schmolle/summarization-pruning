from html.parser import HTMLParser
import gzip
from enum import Enum
import json
import logging
import os
import sys

logfile = '/home/jschmolzi/logs/tools/converter.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile , level=logging.DEBUG)

def find_line_tsv(in_path, qrel_id):
    file_index = 0
    with open(in_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            id, url, title, body = line.split('\t')
            if id == qrel_id:
                print(line)
            
if __name__ == "__main__":
    logging.info("Run started")
    infile = '/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.tsv'
    outfile = '/home/jschmolzi/anserini/collections/base'
    print("logging to %s" % (logfile,))
    print("writing to %s" % (outfile,))
    qrel_id = sys.argv[1]
    
    find_line_tsv(infile, qrel_id)
    
    logging.info("Run finished")
    