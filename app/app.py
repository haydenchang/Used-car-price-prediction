import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")

st.title("Car Price Prediction App")

st.markdown("Enter vehicle details below to get a predicted price:")

# User inputs
year = st.number_input("Year", min_value=1990, max_value=2025, value=2018)
mileage = st.number_input("Mileage", min_value=0, max_value=300000, value=50000)
accidents = st.selectbox("Accident History", ["No accidents", "1 accident", "2+ accidents"])
owners = st.number_input("Number of Previous Owners", min_value=1, max_value=10, value=1)
fuel_type = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Hybrid", "Electric"])
brand = st.text_input("Car Brand", "Toyota")

# Create input DataFrame
input_df = pd.DataFrame({
    "year": [year],
    "mileage": [mileage],
    "accident_history": [accidents],
    "owners": [owners],
    "fuel_type": [fuel_type],
    "brand": [brand]
})

# Prediction
if st.button("Predict Price"):
    predicted_price = model.predict(input_df)[0]
    st.success(f"Estimated Car Price: ${predicted_price:,.2f}")

