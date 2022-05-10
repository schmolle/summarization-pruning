from transformers import pipeline

class Bart():
	_bart = pipeline("summarization", model="facebook/bart-large-cnn")

	def doBart(self, txt):
		return self._bart(txt, max_length=130, min_length=30, do_sample=False)
	