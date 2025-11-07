import streamlit as st
import pandas as pd
import shap
import joblib
from predict import predict_fraud  # Fixed import

# Page configuration
st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

# Title and description
st.title("Fraud Detection System")
st.write("Upload transaction data to detect potential fraudulent transactions.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    # Load uploaded CSV
    data = pd.read_csv(uploaded_file)
    st.write("### Transaction Data Preview")
    st.dataframe(data.head())

    # Run fraud prediction
    st.subheader("🔍 Running Fraud Detection...")
    results = predict_fraud(data)
    st.write("### Prediction Results")
    st.dataframe(results)

    # Load model for SHAP explainability
    try:
        model = joblib.load("model/fraud_model.pkl")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(data)

        st.write("### Feature Importance (SHAP Summary Plot)")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        shap.summary_plot(shap_values[1], data)
        st.pyplot()
    except Exception as e:
        st.error(f"SHAP explanation failed: {e}")

else:
    st.info("Please upload a CSV file to begin fraud detection.")
