from prod_defs import *
import sys
import jsonlines
import json

def absolute_prod(tokens, model):
    print("calling with %d tokens" % (tokens,))
    if model == 'bart':
        inpath = bart_path
    elif model == 'pegasus':
        inpath = pegasus_path
    else:
        inpath = longformer_path
    
    print("infile:", inpath)
    outpath = destination_path
    outpath2 = destination_path_space
    print("outfile:", outpath)
    print("outfile:", outpath2)
    outfile = open(outpath, 'w', encoding='utf-8')
    outfile2 = open(outpath2, 'w', encoding='utf-8')
    with jsonlines.open(inpath, 'r') as infile:
        for line in infile:
            split_contentes = line['contents'].split()
            if len(split_contentes) < tokens:
                continue
            else:
                line['contents'] = (' ').join(split_contentes[0:tokens])
                outfile.write(json.dumps(line) + '\n')
                outfile2.write(json.dumps(line) + '\n')
            break
    outfile.close()
    outfile2.close()
    
    
if __name__ == "__main__":
    usage_string = 'Pass 2 Arguments: NrOfTokens[1,512] Model["bart", "pegasus", "longformer"]'
    if len(sys.argv) != 3:
        print(usage_string)
    try:
        tokens = int(sys.argv[1])
        model = sys.argv[2].lower()
    except Exception as e:
        print(usage_string, e)
    if 1 <= tokens <= 512:
        if model not in ["bart", "pegasus", "longformer"]:
            print(usage_string)
        else:
            absolute_prod(tokens, model)
    else:
        print(usage_string)
    