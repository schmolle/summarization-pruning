import gzip
import torch
import timeit
import logging
import os
import logging.handlers

if os.name == 'nt':
	logfile = "../logs/times.log"
else:
	logfile = "/home/jschmolzi/logs/tools/times.log"
	
should_roll_over = os.path.isfile(logfile)
handler = logging.handlers.RotatingFileHandler(logfile, mode='w', backupCount=5)
if should_roll_over:  # log already exists, roll over!
    handler.doRollover()
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, level=logging.DEBUG)




pegasus_activate = False
bart_activate = False
longformer_activate = True
bigbird_active = False

command_list = []
runs = 20


#init Pegasus
if pegasus_activate:
	from summarize import Pegasus_Impl
	from summarize import Pegasus_Impl_With_Pipeline
	
	pegasus = Pegasus_Impl.Pegasus()
	command_list.append("pegasus.summarize(txt)")
	
	pegasus_pipeline = Pegasus_Impl_With_Pipeline.PegasusWithPipeline()
	command_list.append("pegasus_pipeline.summarize(txt)")

#init Bart
if bart_activate:
	from summarize import Bart_Impl
	from summarize import Bart_Impl_With_Pipeline
	
	bart = Bart_Impl.Bart()
	command_list.append("bart.summarize(txt)")
	
	bart_pipeline = Bart_Impl_With_Pipeline.BartWithPipeline()
	command_list.append("bart_pipeline.summarize(txt)")
	# command_list.append("bart.summarize2(txt)")

#init Longformer
if longformer_activate:
	from summarize import Longformer_Impl
	from summarize import Longformer_Impl_With_Pipeline
	
	longformer = Longformer_Impl.Longformer()
	command_list.append("longformer.summarize(txt)")
	
	longformer_pipeline = Longformer_Impl_With_Pipeline.LongformerWithPipeline()
	command_list.append("longformer_pipeline.summarize(txt)")

#init bigbird
if bigbird_active:
	from summarize import Bigbird_Impl
	from summarize import Bigbird_Impl_With_Pipeline
	
	bigbird = Bigbird_Impl.BigBird()
	command_list.append("bigbird.summarize(txt)")
	
	bigbird_pipeline = Bigbird_Impl_With_Pipeline.BigBirdWithPipeline()
	command_list.append("bigbird_pipeline.summarize(txt)")


if __name__ == '__main__':
	txt = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''
	# init pegasus
	logging.info("###################################################################")
	logging.info("Executing: %s" % (command_list,))
	print('Logging to %s' % (logfile,))
	for command in command_list:
		try:
			logging.info("calling command %s" % (command,))
			time = timeit.timeit(command, globals=locals(), number=runs)
			logging.info("%s called %d times took %ss per run, %ss in total" % (command, runs, format(time/runs, '.4f'), format(time, '.4f')))
		except Exception as e:
			logging.warning("Error: %s in command %s" % (e,command))
		
	# print(doBigBird(txt))