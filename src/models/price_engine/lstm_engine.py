import tensorflow as tf
from typing import List, Dict
import numpy as np

class LSTMPriceEngine:
    def __init__(self, config: Dict):
        self.sequence_length = config["sequence_length"]
        self.n_features = config["n_features"]
        self.model = self._build_model()
        
    def _build_model(self) -> tf.keras.Model:
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(50, return_sequences=True, 
                               input_shape=(self.sequence_length, self.n_features)),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.LSTM(50, return_sequences=True),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.LSTM(50),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model
        
    async def predict(self, data: np.ndarray) -> np.ndarray:
        return self.model.predict(data) 