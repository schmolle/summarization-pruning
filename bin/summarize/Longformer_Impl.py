from transformers import LEDForConditionalGeneration, LEDTokenizer
import torch


class Longformer():
	
	def __init__(self):
		self._tokenizer = LEDTokenizer.from_pretrained("allenai/led-large-16384-arxiv")
		self._model = LEDForConditionalGeneration.from_pretrained("allenai/led-large-16384-arxiv", return_dict_in_generate=True).to("cuda")
		
	def summarize(self, txt):

		input_ids = self._tokenizer(txt, return_tensors="pt").input_ids
		global_attention_mask = torch.zeros_like(input_ids)
		# set global_attention_mask on first token
		global_attention_mask[:, 0] = 1
				
		#sequences = self._model.generate(input_ids, global_attention_mask=global_attention_mask).sequences
		
		#summary = self._tokenizer.batch_decode(sequences)
		summary = ''
		return summary
