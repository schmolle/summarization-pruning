from qrel_defs import qrel10_file_path
from read_10qrels import read_qrels
    
if __name__ == '__main__':
    relevant_qrels = read_qrels()
    print(relevant_qrels[0])
    print(relevant_qrels[1])
    print(relevant_qrels[-1])
    print(len(relevant_qrels))