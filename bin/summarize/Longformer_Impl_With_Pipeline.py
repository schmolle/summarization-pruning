from transformers import pipeline

class LongformerWithPipeline():
    _Longformer = None

    def __init__(self, device=0):
        model_name = "allenai/led-large-16384-arxiv"
        self._Longformer = pipeline("summarization", model=model_name, device=device)  

    def summarize(self, txt, max_length=50, min_length=30):
        return self._Longformer(txt, max_length=max_length, min_length=min_length, do_sample=False, truncation=True)
    