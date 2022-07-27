from qrel_defs import qrel10_file_path

def read_qrels():
    inpath = qrel10_file_path
    with open(qrel_file_path, 'r') as infile:
        qrels = []
        for line in infile:
            qrels.append(line.strip())
        return qrels
    
    
if __name__ == '__main__':
    out_arr = read_qrels()
    print(out_arr[0])
    print(out_arr[1])
    print(out_arr[-1])
    print(len(out_arr))