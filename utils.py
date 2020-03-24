import numpy as np
import tensorflow
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import f1_score


class ClassificationReport(Callback):

    def __init__(self, train=(), val=()):
        super(Callback, self).__init__()

        self.xtrain, self.ytrain = train
        self.train_f1 = []

        self.xval, self.yval = val
        self.val_f1 = []

    def on_epoch_end(self, epoch, logs={}):
        train_pred = np.round(self.model.predict(self.xtrain))
        train_f1 = f1_score(self.ytrain, train_pred)
        self.train_f1.append(train_f1)
        val_pred = np.round(self.model.predict(self.xval))
        val_f1 = f1_score(self.yval, val_pred)
        self.val_f1.append(val_f1)

        print('\nEpoch: {} --- Train F1 Score: {}'.format(epoch, train_f1))
        print('\nEpoch: {} --- Valid F1 Score: {}'.format(epoch, val_f1))
