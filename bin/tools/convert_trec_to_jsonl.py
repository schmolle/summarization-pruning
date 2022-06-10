from html.parser import HTMLParser
import gzip
from enum import Enum
import json

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
    counter = 0
    with gzip.open(in_path, 'rt') as infile, open(out_path, 'w+') as outfile:
        trec_parser = TrecParser(outfile)
        for line in infile:
            trec_parser.feed(line)
            counter = counter + 1
            if counter > 500:
                break
            
if __name__ == "__main__":
    convert_trec_to_jsonl('/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz',
                          '/home/jschmolzi/anserini/collections/msmarco-doc-json-base/msmarco-docs.jsonl')
    