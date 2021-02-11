import os
import pickle
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)
MODEL_PATH = os.path.join('app', 'engine', 'saved_models', 'iris', 'model.pkl')

model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
  features = request.json
  np_features = [
                  np.array([features['sepal_lenght'],
                  features['sepal_width'],
                  features['petal_length'],
                  features['petal_width']])
                ]

  prediction = model.predict(np_features)
  output = prediction[0]

  return jsonify({'prediction': output})
