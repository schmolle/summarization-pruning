from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration

class Bart():
	_bart = pipeline("summarization", model="facebook/bart-large-cnn")
	
	def __init__(self):
		model_name = "facebook/bart-large-cnn"
		self._device = "cuda"
		self._tokenizer = BartTokenizer.from_pretrained(model_name)
		self._model = BartForConditionalGeneration.from_pretrained(model_name).to(self._device)	
	
	def summarize(self, txt):
		src_text = txt
		batch = self._tokenizer(txt, return_tensors="pt").to(self._device)
		generated_ids = self._model.generate(batch["input_ids"])
		tgt_text = self._tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
		return tgt_text
		   
	def summarize2(self, txt):
		return self._bart(txt, max_length=130, min_length=30, do_sample=False)
	