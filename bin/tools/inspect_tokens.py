import os
import jsonlines
from transformers import LEDTokenizer


tokenizer = LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv")
base_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base'
max_tokens = 16384 - 50
too_long_counter_all = 0
for filename in os.listdir(base_path):
    with jsonlines.open(os.path.join(base_path, filename), 'r') as infile:
        too_long_counter = 0
        for line in infile:
            line = line['contents']
            input_ids = tokenizer(line, return_tensors="pt").input_ids.to("cuda")
            line_length = len(input_ids)
            if line_length > max_tokens:
                too_long_counter = too_long_counter + 1
        too_long_counter_all = too_long_counter_all + too_long_counter
        print('File "%s" has %d too long lines' % (filename, too_long_counter))
print('%d too long files total' % (too_long_counter_all,))