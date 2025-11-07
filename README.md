# fraud-detection-application
Overview
The Fraud Detection Software is a machine learning–driven application developed to automatically identify and prevent fraudulent financial transactions. It integrates Python, Scikit-learn, FastAPI, and Streamlit to provide an end-to-end solution — from data ingestion and model training to prediction and visualisation.
The system uses a Random Forest model trained on historical transaction data to predict the likelihood that a transaction is fraudulent. It analyses key indicators such as transaction amount, device type, IP behaviour, location distance, and merchant category, identifying hidden patterns that often signal fraudulent activity.
Key Features
•	AI-Powered Prediction:
Employs supervised machine learning to classify each transaction as “fraudulent” or “legitimate.”
•	Explainable AI (XAI):
Uses SHAP (Shapley Additive exPlanations) to show which features most influence each fraud prediction, promoting transparency and trust.
•	Dual Interface:
o	API Interface (FastAPI): Enables businesses to integrate fraud detection directly into their systems for real-time analysis.
o	Streamlit Dashboard: Provides a user-friendly interface where users can upload data, visualize predictions, and interpret insights.
•	Scalable Design:
Supports both batch processing (large transaction files) and real-time fraud prediction through API calls.
•	Deployable Anywhere:
The software includes a Dockerfile, making it simple to deploy on cloud platforms or local servers.


How to Use the Application
1.	Train the Model
Run the following command to train the fraud detection model using sample or real transaction data:
2.	python train_model.py
This process creates and saves a trained model file inside the /model directory.
3.	Start the API (Backend)
Launch the fraud detection API to enable real-time predictions:
4.	uvicorn api:app --reload --port 8000
Once active, you can send transaction data to the API endpoint to receive fraud risk scores.
5.	Launch the Streamlit Dashboard (Frontend)
To use the graphical interface, run:
6.	streamlit run app.py
Then open the local URL provided (e.g., http://localhost:8501).
o	Upload a CSV file containing transaction data.
o	Click “Run Predictions” to generate fraud classifications and risk scores.
o	View interactive SHAP visualisations showing which features influenced each prediction.
o	Alternatively, you can manually input a single transaction to test in real time.
7.	Interpret the Results
o	Transactions with higher fraud scores (close to 1.0) indicate greater risk.
o	The SHAP summary plot helps you identify the most influential variables — for example, unusually high transaction amounts or distant geolocations.
Real-World Applications
•	Banks and Fintech Companies: Detect suspicious account or transfer activity.
•	E-Commerce Platforms: Identify fake or high-risk purchases and reduce chargebacks.
•	Insurance Firms: Analyze claims to flag potential fraud.
•	Telecoms and Utility Companies: Detect anomalies in billing or usage behavior.

Impact
By automating fraud analysis, this software minimizes human error, reduces manual investigation time, and increases detection accuracy. The use of explainable AI ensures that results are transparent and understandable, supporting ethical AI practices.
The solution provides a scalable, data-driven framework that empowers organizations to make smarter, faster, and more reliable fraud prevention decisions.

