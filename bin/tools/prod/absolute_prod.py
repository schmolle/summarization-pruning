from prod_defs import *
import sys
if __name == "__main__":
    usage_string = 'Pass 1 Argument: nr of Tokens [1,512]'
    if len(sys.args) != 2:
        print(usage_string)
    try:
        tokens = int(sys.args[1])
    except Exception as e:
        print(usage_string, e)
    if 1 <= tokens <= 512:
        absolute_prod(tokens)
    else:
        print(usage_string)
    