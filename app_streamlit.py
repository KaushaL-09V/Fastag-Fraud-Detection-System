import streamlit as st
import requests

st.title("🚗 Fastag Fraud Detection System")

# ===== Dropdowns =====
vehicle_type = st.selectbox("Vehicle Type", ["Car", "Bus", "Truck", "Van", "SUV", "Sedan", "Motorcycle"])
tollbooth = st.selectbox("Toll Booth", ["A-101", "B-102", "C-103", "D-104", "D-105", "D-106"])
lane_type = st.selectbox("Lane Type", ["Express", "Regular"])
vehicle_dim = st.selectbox("Vehicle Dimension", ["Small", "Medium", "Large"])

# ===== Numeric Inputs =====
transaction_amount = st.number_input("Transaction Amount", min_value=0)
amount_paid = st.number_input("Amount Paid", min_value=0)
vehicle_speed = st.number_input("Vehicle Speed", min_value=0)

hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)

latitude = st.number_input("Latitude", value=13.05)
longitude = st.number_input("Longitude", value=77.77)

# ===== Predict =====
if st.button("Predict"):

    data = {
        "Vehicle_Type": vehicle_type,
        "TollBoothID": tollbooth,
        "Lane_Type": lane_type,
        "Vehicle_Dimensions": vehicle_dim,
        "Transaction_Amount": transaction_amount,
        "Amount_paid": amount_paid,
        "Vehicle_Speed": vehicle_speed,
        "Hour": hour,
        "Day": day,
        "Month": month,
        "Latitude": latitude,
        "Longitude": longitude
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=data)

    result = response.json()['prediction']

    if result == "Fraud":
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Not Fraud")