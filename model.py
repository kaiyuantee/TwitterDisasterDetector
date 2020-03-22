import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import RidgeClassifier



class Baseline:
    def __init__(self):
        self.cv = CountVectorizer()
        self.clf = RidgeClassifier()

    def transform(self, x):

        if 'target' in x:
            return self.cv.fit_transform(x.cleaned.str.lower()).todense()
        else:
            return self.cv.transform(x.cleaned.str.lower()).todense()

    def fit(self, x, y):

        self.clf.fit(x, y)

    def predict(self, x):

        return self.clf.predict(x)
