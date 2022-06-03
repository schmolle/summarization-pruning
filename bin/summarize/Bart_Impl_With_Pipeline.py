from transformers import pipeline

class BartWithPipeline():
    _bart = None

    def __init__(self):
        model_name = "facebook/bart-large-cnn"
        self._Bart = pipeline("summarization", model=model_name, device=0)      

    def summarize(self, txt):
        return self._Bart(txt, max_length=130, min_length=30, do_sample=False)
