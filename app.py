from flask import Flask, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

model = pickle.load(open('pipeline_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Fastag Fraud Detection API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    result = "Fraud" if prediction == 1 else "Not Fraud"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
