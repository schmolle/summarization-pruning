import gzip
from transformers import pipeline

with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
	l1 = f.readline()
	l1 = l1[0:1024]
	
	l2 = f.readline()
	l2 = l2[0:1024]

	summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
	
	print(l1)
	print(summarizer(l1, max_length=130, min_length=30, do_sample=False))
	print("---------------------------------------------------------")
	print(l2)

	print(summarizer(l2, max_length=130, min_length=30, do_sample=False))