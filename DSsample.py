from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, resources={r"/prediction": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/stats": {"origins": "http://localhost:3000"}})
def calculate_statistics():
    data = pd.read_csv("C:/Users/kaush/Downloads/DS/data.csv")
    statistics={}
    statistics["nitrogen"]="Average Ratio of Nitrogen in the Soil : {0:.2f}".format(data['N'].mean())
    statistics["Phosporous"]="Average Ratio of Phosphorous in the Soil : {0:.2f}".format(data ['P'].mean ())
    statistics["Potassium"]="Average Ratio of Potassium in the Soil: {0:.2f}".format (data['K'].mean())
    statistics["Temperature"]="Average Tempature in Celsius : {0:.2f}".format (data['temperature'].mean ())
    statistics["Humidity"]="Average Relative Humidity in % : {0:.2f}".format (data ['humidity'].mean ())
    statistics["PHValue"]="Average PH Value of the soil: {0:.2f}".format (data[ 'ph'].mean ())
    statistics["Rainfall"]="Average Rainfall in mm : {0: .2f}".format(data ['rainfall'].mean ())
    return statistics

with open('knn_clf.pkl', 'rb') as model_file:
    knn_model = pickle.load(model_file)


@app.route('/stats', methods=['GET'])
def get_crop_statistics():
    statistics = calculate_statistics()
    return jsonify(statistics)
    
@app.route('/prediction', methods=['POST'])
def get_prediction():
    data = request.get_json()
    if isinstance(data, list):
        data_array = np.array(data).reshape(1, -1)
        predictions = knn_model.predict(data_array)
        return jsonify(predictions.tolist())
    else:
        return jsonify({"error": "Invalid data format"}), 400


if __name__ == '__main__':
    app.run(port=5000)