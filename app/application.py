import os
import pickle
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)
MODEL_PATH = os.path.join('app', 'engine', 'saved_models', 'iris', 'model.pkl')

model = pickle.load(open(MODEL_PATH, 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
  int_features = [float(x) for x in request.form.values()]
  np_features = [np.array(int_features)]

  prediction = model.predict(np_features)
  output = prediction[0]

  return jsonify({'prediction': output})
