from transformers import PegasusForConditionalGeneration, PegasusTokenizer

class Pegasus():
	_tokenizerP = None
	_modelP = None
	_device = None

	def __init__(self):
		model_name = "google/pegasus-xsum"
		self._device = "cpu"
		self._tokenizerP = PegasusTokenizer.from_pretrained(model_name)
		self._modelP = PegasusForConditionalGeneration.from_pretrained(model_name).to(self._device)

	def summarize(self, txt):
		src_text = txt
		batch = self._tokenizerP(src_text, truncation=True, padding="longest", return_tensors="pt").to(self._device)
		translated = self._modelP.generate(**batch)
		tgt_text = self._tokenizerP.batch_decode(translated, skip_special_tokens=True)
		return tgt_text