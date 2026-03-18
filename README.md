# 🚗 Fastag Fraud Detection System

## 📌 Overview

This project is an end-to-end Machine Learning system designed to detect fraudulent Fastag transactions. It includes data preprocessing, model training, and deployment using Flask (backend API) and Streamlit (frontend UI).

---

## 🎯 Problem Statement

Fastag systems enable automated toll collection, but fraudulent activities such as underpayment or misuse of lanes lead to revenue loss.

This project aims to:

* Detect fraudulent transactions
* Minimize financial loss
* Provide real-time predictions

---

## 🧠 Solution Approach

### 1. Data Preprocessing

* Handled missing values
* Extracted time-based features (Hour, Day, Month)
* Converted geographical coordinates
* Removed irrelevant columns
* Encoded categorical features using OneHotEncoder

### 2. Feature Engineering

* Extracted meaningful features from timestamp and location
* Used transaction patterns to detect anomalies

### 3. Handling Imbalance

* Applied **SMOTE** to balance fraud and non-fraud cases

### 4. Model Building

* Models used:
  * Logistic Regression
  * Decision Tree
  * Random Forest (final model)

### 5. Pipeline

* Used `ColumnTransformer` and `Pipeline`
* Integrated preprocessing + SMOTE + model

---

## 📊 Model Performance

* High Recall for Fraud Detection
* Balanced Precision and F1-score
* Robust performance on unseen data

---

## 🚀 Deployment

### 🔹 Backend (Flask API)

* Handles prediction requests
* Accepts JSON input
* Returns Fraud / Not Fraud

### 🔹 Frontend (Streamlit)

* User-friendly UI
* Dropdowns for categorical inputs
* Real-time prediction display

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Flask
* Streamlit

---

## 📂 Project Structure

```
├── app.py                # Flask API
├── app_streamlit.py     # Streamlit UI
├── pipeline_model.pkl   # Trained ML pipeline
├── fastag_fraud.csv     # Dataset
├── requirements.txt     # Dependencies
├── README.md
├── .gitignore
```

---

## ▶️ How to Run Locally

### 1. Clone Repository

```
git clone <your-repo-link>
cd fastag-fraud-detection
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Flask API

```
python app.py
```

### 4. Run Streamlit App

```
streamlit run app_streamlit.py
```

---

## 🌐 Future Improvements

* Remove data leakage completely
* Deploy on cloud (Render / AWS)
* Add real-time streaming data
* Improve model with XGBoost

---

## 👨‍💻 Author

Kaushal Vadher
