import os
import jsonlines

base_path = '/home/jschmolzi/anserini/collections/msmarco-doc-json-base'
max_tokens = 16384 - 50
too_long_counter_all = 0
for filename in os.listdir(base_path):
    with jsonlines.open(filename, 'r') as infile:
        for line in infile:
            too_long_counter = 0
            line_arr = line.split()
            line_length = len(line_arr)
            if line_length > max_tokens:
                too_long_counter = too_long_counter + 1
        too_long_counter_all = too_long_counter_all + too_long_counter
        print('File "%s" has %d too long lines' %s (base_path.split[-1], ))
print('%d too long files total' % (too_long_counter_all,))