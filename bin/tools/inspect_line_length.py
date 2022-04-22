import gzip

counter = 0;
max_length = 0;
min_length = 0;
longer1024 = 0;

with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
	for line in f:
		length = len(line)
		if length < min_length: min_length = length
		if length > max_length: max_length = length
		if length > 1024: longer1024++
        counter++;