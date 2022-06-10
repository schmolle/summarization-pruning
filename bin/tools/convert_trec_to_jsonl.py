from html.parser import HTMLParser
import gzip
from enum import Enum

class Mode(Enum):
    UNDEF = 0
    TEXT = 1
    DOCNO = 2
    DOC = 3
    
    
class TrecParser(HTMLParser):
    current_text = ''
    current_id = ''
    mode = Mode.UNDEF
    
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
            print('Ended Doc')
            print('ID :', self.current_id)
            print('content :', self.current_text)
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


def convert_trec_to_jsonl(path):
    counter = 0
    with gzip.open(path, 'rt') as f:
        trec_parser = TrecParser()
        for line in f:
            trec_parser.feed(line)
            counter = counter + 1
            if counter > 500:
                break
            
if __name__ == "__main__":
    convert_trec_to_jsonl('/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz')
    