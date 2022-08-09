from html.parser import HTMLParser
import gzip
from enum import Enum
import json
import logging

logfile = '/home/jschmolzi/logs/tools/converter.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile , level=logging.DEBUG)

class Mode(Enum):
    UNDEF = 0
    TEXT = 1
    DOCNO = 2
    DOC = 3
    
    
class TrecParser(HTMLParser):
    current_text = ''
    current_id = ''
    mode = Mode.UNDEF
    outfile = None
    doc_counter = 0
    
    def __init__(self, outfile):
        HTMLParser.__init__(self)
        self.outfile = outfile
        
    def handle_starttag(self, tag, attrs):
        if tag == 'text':
            self.mode = Mode.TEXT
        elif tag == 'docno':
            self.mode = Mode.DOCNO
        elif tag == 'doc':
            self.mode = Mode.DOC
            
    def handle_endtag(self, tag):
        self.mode = Mode.UNDEF
        if tag == 'doc':
            # print('Ended Doc')
            # print('ID :', self.current_id)
            # print('content :', self.current_text)
            data_dict = {'id' : self.current_id, 'body' : self.current_text}
            write_jsonl(self.outfile, data_dict)
            self.current_text = ''
            self.doc_counter = self.doc_counter + 1

    def handle_data(self, data):
        data = data.strip().replace('\n','')
        if self.mode == Mode.TEXT:
            if self.current_text != '':
                self.current_text = self.current_text + ' ' + data
            else:
                self.current_text = data
        elif self.mode == Mode.DOCNO:
            self.current_id = data


def write_jsonl(outfile, data):
    outfile.write(json.dumps(data) + "\n")

def convert_trec_to_jsonl(in_path, out_path):
    logging.info("############################################################################")
    logging.info("started run")
    counter = 0
    last_counter = 0
    try:
        with gzip.open(in_path, 'rt') as infile, open(out_path, 'w+') as outfile:
            trec_parser = TrecParser(outfile)
            for line in infile:
                try:
                    trec_parser.feed(line)
                    counter = counter + 1
                    if (counter - 100,000) >= last_counter:
                        logging.info("Parsed %d lines" % (counter,))
                        last_counter = counter
                except Exception as e:
                    logging.error("Error in Line: %s" % (e,))
    except Exception as e:
        logging.error("Error in Function: %s" % (e,))
    logging.info("Parsed %d lines" % (counter,))
    logging.info("ended run")
            
if __name__ == "__main__":
    infile = '/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz'
    outfile = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/msmarco-docs.jsonl'
    print("logging to %s" % (logfile,))
    print("writing to %s" % (outfile,))
    
    convert_trec_to_jsonl(infile, outfile)
    