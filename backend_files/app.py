
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("superkart_model.joblib")

@app.route("/v1/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return jsonify(
        {"predicted_sales": float(prediction[0])}
    )

@app.route("/v1/predictbatch", methods=["POST"])
def predict_batch():

    file = request.files["file"]

    df = pd.read_csv(file)

    predictions = model.predict(df)

    result = {
        str(i): float(pred)
        for i, pred in enumerate(predictions)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
