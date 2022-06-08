from html.parser import HTMLParser

class TrecParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def convert_trec_to_jsonl(path):
    counter = 0
    with gzip.open(path, 'r') as f:
        for line in f:
            print(line)
            trec_parser = TrecParser()
            trec_parser.feed(line)
            counter = counter + 1
            if counter > 34:
                break
            
if __name__ == 'main':
    convert_trec_to_jsonl('/home/jschmolzi/anserini/collections/msmarco-doc/msmarco-docs.trec.gz')