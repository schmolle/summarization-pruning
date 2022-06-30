from qrel_defs import qrel_file_path

def filter_qrel_ids(inpath, outpath):
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        for line in infile:
            line_array = line.split('\t')
            print(line_array)
            qrel_id = line_array[2]
            print(qrel_id)
            outfile.write(qrel_id + '\n')
            break

if __name__ == "__main__":
    inpath = '/home/jschmolzi/anserini/src/main/resources/topics-and-qrels/qrels.msmarco-doc.dev.txt'
    outpath = qrel_file_path
    filter_qrel_ids(inpath, outpath)