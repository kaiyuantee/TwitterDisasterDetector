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
from .model import DisasterDetector
from .dataset import read_dataset


def main():

    train, test, sub = read_dataset()
    bert_layer = hub.KerasLayer('https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/1', trainable=True)
    clf = DisasterDetector(bert_layer,
                           max_sql=128,
                           lr=0.000005,
                           epochs=3,
                           batch_size=16)
    clf.fit(train)
    sub['target'] = np.round(clf.predict(test)).astype('int')
    sub.to_csv('submission.csv', index=False)


if __name__ == '__main__':
    main()
