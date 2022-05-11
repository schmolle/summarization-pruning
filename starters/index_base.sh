#!/bin/bash

sh /home/jschmolzi/anserini/target/appassembler/bin/IndexCollection -threads 3 -collection CleanTrecCollection \
 -generator DefaultLuceneDocumentGenerator -input /home/jschmolzi/data/msmarco-doc \
 -index ~/indexes/msmarco/base -storePositions -storeDocvectors -storeRaw
 