from transformers import pipeline

class LongformerWithPipeline():
    _Longformer = None

    def __init__(self):
        model_name = "allenai/led-large-16384-arxiv"
        self._Longformer = pipeline("summarization", model=model_name, device=0)  

    def summarize(self, txt):
        return self._Longformer(txt, max_length=130, min_length=30, do_sample=False)
