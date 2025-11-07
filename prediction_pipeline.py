import joblib
from predict import predict_fraud

MODEL_PATH = "model/fraud_model.pkl"

def run_prediction(df):
    """
    Run fraud detection using trained model.
    """
    model = joblib.load(MODEL_PATH)
    predictions = predict_fraud(df)
    return predictions
