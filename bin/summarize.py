import gzip

with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
    print(f.readline())