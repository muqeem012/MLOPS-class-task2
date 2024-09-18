from flask import Flask, jsonify, request
import joblib
import numpy as np
from flask_cors import CORS

model = joblib.load("model")

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
def predictController():
    requestData = request.get_json()
    area = requestData["area"]
    bedrooms = requestData["bedrooms"]
    bathrooms = requestData["bathrooms"]
    stories = requestData["stories"]
    predictedPrice = model.predict(np.array([[area, bedrooms, bathrooms, stories]]))
    response = {}
    response["prediction"] = float(predictedPrice[0])
    return jsonify(response),200


if __name__ == '__main__':
     app.run(port="9000", host="0.0.0.0")
