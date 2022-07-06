from qrel_defs import qrel_file_path

def filter_qrel_ids(inpath, outpath):
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        for line in infile:
            line_array = line.split('\t')
            qrel_id = line_array[2]
            outfile.write(qrel_id.strip() + '\n')

if __name__ == "__main__":
    inpath = '/home/jschmolzi/anserini/src/main/resources/topics-and-qrels/qrels.msmarco-doc.dev.txt'
    outpath = qrel_file_path
    filter_qrel_ids(inpath, outpath)