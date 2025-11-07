import joblib
import pandas as pd

def predict_fraud(dataframe):
    model = joblib.load("model/fraud_model.pkl")
    predictions = model.predict(dataframe)
    dataframe["Prediction"] = ["Fraud" if p == 1 else "Legit" for p in predictions]
    return dataframe
