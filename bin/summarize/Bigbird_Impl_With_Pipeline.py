from transformers import pipeline

class BigBirdWithPipeline():
    _BigBird = None

    def __init__(self):
        model_name = "google/bigbird-pegasus-large-arxiv"
        self._BigBird = pipeline("summarization", model=model_name, device=0)
        
    def summarize(self, txt):
        return self._BigBird(txt, max_length=130, min_length=30, do_sample=False)
