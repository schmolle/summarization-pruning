import gzip
from transformers import pipeline
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


def doPegasus(txt):
	src_text = """ PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."""
	src_text = txt
	model_name = "google/pegasus-xsum"
	device = "cpu"
	tokenizer = PegasusTokenizer.from_pretrained(model_name)
	model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
	batch = tokenizer(src_text, truncation=True, padding="longest", return_tensors="pt").to(device)
	translated = model.generate(**batch)
	tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
	return tgt_text

def doBart(txt):
	text = text[0:1024]
	summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

with gzip.open('/data/ms-marco/fulldocs.tsv.gz','rt') as f:
	l1 = f.readline()
	print("L1 length" % (len(l1),))
	l1 = doBart(l1)
	print(l1)

	l2 = f.readline()
	print("L2 length" % (len(l2),))
	l2 = doPegasus(l2)
	print(l2)