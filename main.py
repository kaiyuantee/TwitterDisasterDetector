import numpy as np
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from .model import Baseline
from .dataset import read_dataset


def main():

    train, test, sub = read_dataset()
    clf = Baseline()
    xtrain, ytrain = clf.transform(train)
    clf.fit(xtrain, ytrain)
    xtest = clf.transform(test)
    sub['target'] = np.round(clf.predict(xtest)).astype('int')
    sub.to_csv('submission.csv', index=False)


if __name__ == '__main__':
    main()
