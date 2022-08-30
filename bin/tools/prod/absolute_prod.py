from prod_defs import *
import sys

def absolute_prod(tokens):
    print("calling with %d tokens" % (tokens,))
if __name__ == "__main__":
    usage_string = 'Pass 1 Argument: nr of Tokens [1,512]'
    if len(sys.argv) != 2:
        print(usage_string)
    try:
        tokens = int(sys.argv[1])
    except Exception as e:
        print(usage_string, e)
    if 1 <= tokens <= 512:
        absolute_prod(tokens)
    else:
        print(usage_string)
    