import pandas as pd
import numpy as np
from sklearn.metrics import f1_score
from bert.tokenization import FullTokenizer
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.layers import Input,Dense
from tensorflow.keras.models import Model
from sklearn.model_selection import StratifiedKFold
from .utils import ClassificationReport


class DisasterDetector:
    def __init__(self, bert_layer, max_sql, lr, batch_size, epochs):

        self.bert_layer = bert_layer
        self.max_sql = max_sql
        vocab = self.bert_layer.resolved_object.vocab_file.asset_path.numpy()
        lowercase = self.bert_layer.resolved_object.do_lower_case.numpy()
        self.token = FullTokenizer(vocab, lowercase)
        self.lr = lr
        self.batch_size = batch_size
        self.epochs = epochs
        self.models = []
        self.scores = {}

    def encode(self, texts):

        all_tokens = []
        all_masks = []
        all_segments = []
        for text in texts:
            text = self.token.tokenize(text)
            text = text[:self.max_sql - 2]
            input_seq = ['[CLS]'] + text + ['[SEP]']
            pad_len = self.max_sql - len(input_seq)
            tokens = self.token.convert_tokens_to_ids(input_seq)
            tokens += [0] * pad_len
            pad_masks = [1] * len(input_seq) + [0] * pad_len
            segment_ids = [0] * self.max_sql
            all_tokens.append(tokens)
            all_masks.append(pad_masks)
            all_segments.append(segment_ids)
        return np.array(all_tokens), np.array(all_masks), np.array(all_segments)

    def build_model(self):

        input_words = Input(shape=(self.max_sql,), dtype=tf.int32, name='input_words')
        input_mask = Input(shape=(self.max_sql,), dtype=tf.int32, name='input_mask')
        segmentids = Input(shape=(self.max_sql,), dtype=tf.int32, name='segment_ids')
        _, sequence_output = self.bert_layer([input_words, input_mask, segmentids])  # without pooled output
        clf_output = sequence_output[:, 0, :]
        out = Dense(1, activation='sigmoid')(clf_output)

        model = Model(inputs=[input_words, input_mask, segmentids], outputs=out)
        optimizer = Adam(learning_rate=self.lr)
        model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return model

    def fit(self, X):
        skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=999)
        for fold, (trn_idx, val_idx) in enumerate(skf.split(X['cleaned'], X['keyword'])):
            print('\nFold {}\n'.format(fold))

            X_trn_encoded = self.encode(X.loc[trn_idx, 'cleaned'].str.lower())
            y_trn = X.loc[trn_idx, 'target_relabeled']
            X_val_encoded = self.encode(X.loc[val_idx, 'cleaned'].str.lower())
            y_val = X.loc[val_idx, 'target_relabeled']

            # Callbacks
            metrics = ClassificationReport(train=(X_trn_encoded, y_trn), val=(X_val_encoded, y_val))

            # Model
            model = self.build_model()
            model.fit(X_trn_encoded, y_trn, validation_data=(X_val_encoded, y_val), callbacks=[metrics],
                      epochs=self.epochs, batch_size=self.batch_size)

            self.models.append(model)
            self.scores[fold] = {
                'train': {
                    'f1': metrics.train_f1
                },
                'validation': {
                    'f1': metrics.val_f1
                }
            }

    def predict(self, X):

        X_test_encoded = self.encode(X['cleaned'].str.lower())
        y_pred = np.zeros((X_test_encoded[0].shape[0], 1))

        for model in self.models:
            y_pred += model.predict(X_test_encoded) / len(self.models)

        return y_pred