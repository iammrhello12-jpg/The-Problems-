import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import random

class SimpleAgent:
    def __init__(self):
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])
        self.responses = {}

    def train(self, data_path):
        df = pd.read_csv(data_path)
        self.pipeline.fit(df['pattern'], df['intent'])

        # Store responses for each intent
        for intent in df['intent'].unique():
            self.responses[intent] = df[df['intent'] == intent]['response'].tolist()

    def predict(self, text):
        intent = self.pipeline.predict([text])[0]
        response = random.choice(self.responses[intent])
        return {"intent": intent, "response": response}

    def save(self, path):
        joblib.dump({"pipeline": self.pipeline, "responses": self.responses}, path)

    def load(self, path):
        data = joblib.load(path)
        self.pipeline = data["pipeline"]
        self.responses = data["responses"]
