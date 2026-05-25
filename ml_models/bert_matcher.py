from sentence_transformers import SentenceTransformer, util

class BERTMatcher:
    def __init__(self):
        # Lazy loading of model to prevent huge boot times when importing
        self.model = None

    def _load_model(self):
        if self.model is None:
            # all-MiniLM-L6-v2 is fast and effective for semantic similarity
            print("Loading BERT SentenceTransformer model... This might take a moment.")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def calculate_similarity(self, resume_text: str, jd_text: str) -> float:
        """
        Calculates cosine similarity between the embedded resume and the embedded
        Job Description using a pre-trained sentence transformer model.
        Returns a float between 0.0 and 1.0.
        """
        self._load_model()
        
        # In a real heavy system, you might chunk the resume text to not exceed context lengths.
        # MiniLM supports up to 256 tokens, but we will pass the whole text and let it truncate 
        # or we could chunk it. For startup MVP, truncation or passing raw works fine.
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)
        
        cosine_score = util.cos_sim(resume_embedding, jd_embedding)
        return float(cosine_score[0][0])

# Singleton
matcher = BERTMatcher()
