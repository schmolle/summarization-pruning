#! /bin/bash

python simple_summarizer.py ~/anserini/collections/msmarco-doc-json-base/docs00aa.json ~/anserini/collections/msmarco-doc-json-00/ ~/logs/tools/summarizer1.log 0 &
python simple_summarizer.py ~/anserini/collections/msmarco-doc-json-base/docs00ab.json ~/anserini/collections/msmarco-doc-json-00/ ~/logs/tools/summarizer2.log 1 &