from read_qrels import read_qrels

if __name__ == '__main__':
    qrel_arr = read_qrels()
    print(len(qrel_arr))
    print(len(set(qrel_arr)))
    
    