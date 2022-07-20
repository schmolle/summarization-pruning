import os
import sys


def find_line_tsv(in_path, qrel_ids):
    file_index = 0
    with open(in_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            id, url, title, body = line.split('\t')
            if id in qrel_ids:
                print(line)
                print("id: %s" % (id,))
                print("url: %s" % (url,))
                print("title: %s" % (title,))
                print("body: %s" % (body))
if __name__ == "__main__":
    nr_inputs = len(sys.argv)
    print("Looking for %s lines" % (nr_inputs-1,))
    qrel_ids = []
    for id in range(1, nr_inputs):
        qrel_ids.append(sys.argv[id])
    print(qrel_ids)
    find_line_tsv(infile, qrel_id)
        