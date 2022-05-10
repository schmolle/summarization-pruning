#!/bin/bash

sh target/appassembler/bin/IndexCollection -threads 1 -collection CleanTrecCollection \
 -generator DefaultLuceneDocumentGenerator -input /data/ms-marco/fulldocs.tsv.gz \
 -index ~/indexes/msmarco/base -storePositions -storeDocvectors -storeRaw