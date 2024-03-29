from prod_defs import *
import sys
import jsonlines
import json
import math


def absolute_prod(tokens, model):
    print("calling with %f tokens" % (tokens,))
    if model == 'bart':
        inpath = bart_path
        max_tokens = 512
    elif model == 'pegasus':
        inpath = pegasus_path
        max_tokens = 256
    else:
        inpath = longformer_path
        max_tokens = 512
    
    print("infile:", inpath)
    outpath = destination_path
    outpath2 = destination_path_space
    print("outfile:", outpath)
    outfile = open(outpath, 'w', encoding='utf-8')
    outfile2 = open(outpath2, 'w', encoding='utf-8')
    with jsonlines.open(inpath, 'r') as infile:
        for line in infile:
            split_contentes = line['contents'].split()
            cur_tokens = math.ceil(len(split_contentes) * tokens)
            if cur_tokens < 5:
                line['contents'] = (' ').join(split_contentes)
            else:
                line['contents'] = (' ').join(split_contentes[0:cur_tokens])
            outfile.write(json.dumps(line) + '\n')
            outfile2.write(json.dumps(line) + '\n')
    outfile.close()
    outfile2.close()

    
if __name__ == "__main__":
    usage_string = 'Pass 2 Arguments: NrOfTokens[0.1, 0.7] Model["bart", "pegasus", "longformer"]'
    if len(sys.argv) != 3:
        print(usage_string)
    try:
        tokens = float(sys.argv[1])
        model = sys.argv[2].lower()
    except Exception as e:
        print(usage_string, e)
    if 0.1 <= tokens <= 0.9:
        if model not in ["bart", "pegasus", "longformer"]:
            print(usage_string)
        else:
            absolute_prod(tokens, model)
    else:
        print(usage_string)
    