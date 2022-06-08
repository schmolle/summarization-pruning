from html.parser import HTMLParser
import gzip
from enum import Enum

class Mode(Enum):
    UNDEF = 0
    TEXT = 1
    ID = 2
    
    
class TrecParser(HTMLParser):
    current_text = 0
    current_id = 0
    mode = 0
    
    def handle_starttag(self, tag, attrs):
        if tag == 'text':
            print("starting text")
        elif tag == 'docno':
            print("starting docno")
        elif tag == 'doc':
            print('starting doc')
            
    def handle_endtag(self, tag):
        if tag == 'doc':
            print("END of doc")

    def handle_data(self, data):
        print("Encountered some data  :", data)


def convert_trec_to_jsonl(path):
    counter = 0
    with gzip.open(path, 'rt') as f:
        for line in f:
            trec_parser = TrecParser()
            trec_parser.feed(line)
            counter = counter + 1
            if counter > 34:
                break
            
if __name__ == "__main__":
    print("start")
    convert_trec_to_jsonl('/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz')
    print("end")