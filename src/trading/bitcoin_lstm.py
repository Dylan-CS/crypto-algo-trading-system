import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from itertools import cycle
from nacos import NacosClient

class BitcoinLSTM:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def load_data(self):
        self.df = pd.read_csv(self.data_path)
        self.df.set_index('Date', inplace=True)

    def preprocess_data(self):
        data = self.df['Close'].values.reshape(-1, 1)
        scaled_data = self.scaler.fit_transform(data)
        X, y = [], []
        for i in range(60, len(scaled_data)):
            X.append(scaled_data[i-60:i, 0])
            y.append(scaled_data[i, 0])
        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))
        return X, y

    def build_model(self):
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(60, 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(units=50))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(units=1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train_model(self, X_train, y_train, epochs=150, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def predict(self, X_test):
        predictions = self.model.predict(X_test)
        return self.scaler.inverse_transform(predictions)

    def predict_bitcoin_price(self, input_data):
        input_data = input_data.reshape(-1, 1)
        input_data = self.scaler.transform(input_data)
        X_test = []
        for i in range(60, input_data.shape[0]):
            X_test.append(input_data[i-60:i, 0])
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predictions = self.model.predict(X_test)
        return self.scaler.inverse_transform(predictions)

    def evaluate_model(self, test_df, predictions):
        mse = mean_squared_error(test_df['Close'].values, predictions)
        mae = mean_absolute_error(test_df['Close'].values, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(test_df['Close'].values, predictions)
        print(f'The Mean Squared Error is {mse}')
        print(f'The Mean Absolute Error is {mae}')
        print(f'The Root Mean Squared Error is {rmse}')
        print(f'The R-squared is: {r2}')