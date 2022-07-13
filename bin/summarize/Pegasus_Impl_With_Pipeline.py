from transformers import pipeline

class PegasusWithPipeline():
    _Pegasus = None

    def __init__(self, device = 0):
        model_name = "google/pegasus-xsum"
        self._Pegasus = pipeline("summarization", model=model_name, device=device)

    def summarize(self, txt, max_length=130, min_length=30):
        return self._Pegasus(txt, max_length=max_length, min_length=min_length, do_sample=False)
