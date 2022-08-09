from html.parser import HTMLParser
import gzip
from enum import Enum
import json
import logging
import os

logfile = '/home/jschmolzi/logs/tools/converter.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile , level=logging.DEBUG)

def convert_tsv_to_jsonl(in_path, out_path, max_lines_per_file):
    file_index = 0
    with open(in_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            id, url, title, body = line.split('\t')

            if i % max_lines_per_file == 0:
                if i > 0:
                    output_jsonl_file.close()
                output_path = os.path.join(out_path, 'docs{:02d}.json'.format(file_index))
                output_jsonl_file = open(output_path, 'w', encoding='utf-8', newline='\n')
                file_index += 1
            output_dict = {'id': id, 'url': url, 'title': title, 'contents': body}
            output_jsonl_file.write(json.dumps(output_dict) + '\n')

            if i % 100000 == 0:
                logging.info(f'Converted {i:,} docs, writing into file {file_index}')

    output_jsonl_file.close()
            
if __name__ == "__main__":
    logging.info("Run started")
    infile = '/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.tsv'
    outfile = '/home/jschmolzi/anserini/collections/base'
    print("logging to %s" % (logfile,))
    print("writing to %s" % (outfile,))
    
    convert_tsv_to_jsonl(infile, outfile, 100000)
    
    logging.info("Run finished")
    