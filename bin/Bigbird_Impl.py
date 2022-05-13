from transformers import BigBirdPegasusForConditionalGeneration, AutoTokenizer

class BigBird():
	_tokenizer = None
	_model = None

	def __init__(self):
		self._tokenizer = AutoTokenizer.from_pretrained("google/bigbird-pegasus-large-arxiv")
		self._model = BigBirdPegasusForConditionalGeneration.from_pretrained("google/bigbird-pegasus-large-arxiv").to("cuda") 

	def summarize(self, txt):
		inputs = self._tokenizer(txt, return_tensors='pt').to("cuda")
		prediction = self._model.generate(**inputs)
		prediction = self._tokenizer.batch_decode(prediction).to("cuda")
		return prediction