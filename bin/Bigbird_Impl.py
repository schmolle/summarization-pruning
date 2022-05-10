from transformers import BigBirdPegasusForConditionalGeneration, AutoTokenizer

class Bigbird():
	_tokenizer = None
	_model = None

	def __init__(self):
		self._tokenizer = AutoTokenizer.from_pretrained("google/bigbird-pegasus-large-arxiv")
		self._model = BigBirdPegasusForConditionalGeneration.from_pretrained("google/bigbird-pegasus-large-arxiv") 

	def doBigBird(self, txt):
		inputs = self._tokenizer(txt, return_tensors='pt')
		prediction = self._model.generate(**inputs)
		prediction = self._tokenizer.batch_decode(prediction)
		return prediction