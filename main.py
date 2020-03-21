import numpy as np
import pandas as pd
import nltk
import string
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
import tensorflow_hub as hub
from .model import DisasterDetector, NaiveBayes
from .dataset import read_dataset


def main():

    train, test, sub = read_dataset()
    clf = NaiveBayes()
    x, y = clf.transform(train)
    clf.fit(x, y)
    sub['target'] = np.round(clf.predict(clf.transform(test))).astype('int')
    sub.to_csv('submission.csv', index=False)


if __name__ == '__main__':
    main()
