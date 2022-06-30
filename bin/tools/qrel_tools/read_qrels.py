from qrel_defs import qrel_file_path

def read_qrels():
    inpath = qrel_file_path
    with open(qrel_file_path, 'r') as infile:
        qrels = []
        for line in infile:
            qrels.append(line.strip())
        print(qrels) 