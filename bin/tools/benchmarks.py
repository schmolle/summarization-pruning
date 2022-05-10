import gzip
import torch
import timeit
import logging

#needed for imports
import sys
sys.path.append("..")

import Bart_Impl
import Longformer_Impl
import Pegasus_Impl
import Bigbird_Impl


logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/jschmolzi/logs/tools/times.log', level=logging.DEBUG)

pegasus_activate = True
bart_activate = True
longformer_activate = False
bigbird_active = True

command_list = []
runs = 20
#init Pegasus
if pegasus_activate:
	pegasus = Pegasus_Impl.Pegasus()
	command_list.append("pegasus.summarize(txt)")

#init Bart
if bart_activate:
	bart = Bart_Impl.Bart()
	command_list.append("bart.summarize(txt)")

#init Longformer
#if longformer_activate:
#	model_long = LongformerModel.from_pretrained('longformer-base-4096')
#	tokenizer_long = RobertaTokenizer.from_pretrained('roberta-base')
#	tokenizer_long.model_max_length = model_long.config.max_position_embeddings
#	command_list.append("doLongformer(txt)")

#init bigbird
if bigbird_active:
	bigbird = Bigbird_Impl.BigBird()
	command_list.append("bigbird.summarize(txt)")


if __name__ == '__main__':
	txt = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''
	# init pegasus
	logging.info("###################################################################")
	logging.info(command_list)
	for command in command_list:
		try:
			logging.info("calling command %s" % (command,))
			time = timeit.timeit(command, globals=locals(), number=runs)
			logging.info("%s called %d times took %ss per run, %ss in total" % (command, runs, time/runs, time))
		except Exception as e:
			logging.warning("Error: %s in command %s" % (e,command))
		
	# print(doBigBird(txt))