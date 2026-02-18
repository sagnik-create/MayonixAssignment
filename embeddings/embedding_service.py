from sklearn.feature_extraction.text import TfidfVectorizer

class EmbeddingService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.fitted = False

    def fit(self, texts):
        self.vectorizer.fit(texts)
        self.fitted = True

    def embed(self, texts):
        if not self.fitted:
            raise ValueError("Vectorizer not fitted yet. Call fit() first.")
        return self.vectorizer.transform(texts).toarray()
