from pipelines.data_pipeline import load_transactions, clean_data, feature_engineering
from pipelines.prediction_pipeline import run_prediction
import pandas as pd

def main():
    # 1️⃣ Load data
    df = load_transactions()  # loads all CSVs in 'data/'
    print("Data loaded:", df.shape)

    # 2️⃣ Clean data
    df = clean_data(df)
    print("Data cleaned:", df.shape)

    # 3️⃣ Feature engineering
    df = feature_engineering(df)
    print("Features created.")

    # 4️⃣ Run prediction
    results = run_prediction(df)
    print("Predictions done.")

    # 5️⃣ Save results
    df['fraud_prediction'] = results
    df.to_csv("data/predicted_transactions.csv", index=False)
    print("Results saved to data/predicted_transactions.csv")

if __name__ == "__main__":
    main()
