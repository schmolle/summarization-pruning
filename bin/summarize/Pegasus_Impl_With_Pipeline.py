from transformers import pipeline

class PegasusWithPipeline():
    _Pegasus = None

    def __init__(self):
        model_name = "google/pegasus-xsum"
        self._Pegasus = pipeline("summarization", model=model_name, device=0)

    def summarize(self, txt):
        return self._Pegasus(txt, max_length=130, min_length=30, do_sample=False)
