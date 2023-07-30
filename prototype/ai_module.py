import tensorflow as tf
from prototype.data_analysis import data_set
from prototype.machine_learning import analyzeData

class AIModule:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=[len(data_set.keys())]),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    def train_model(self, dataset, labels, epochs):
        history = self.model.fit(
            dataset, labels,
            epochs=epochs, validation_split=0.2, verbose=0)
        return history

    def predict(self, input_data):
        return self.model.predict(input_data)

    def analyze_data(self):
        analyzed_data = analyzeData(data_set)
        return analyzed_data

ai_module = AIModule()