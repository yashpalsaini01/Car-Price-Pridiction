
import streamlit as st
import pickle
import pandas as pd

with open("car.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details below to predict its selling price.")


car_names = [
    "Maruti Swift",
    "Hyundai i20",
    "Honda City",
    "Toyota Innova",
    "Mahindra Scorpio",
    "BMW 3 Series",
    "Audi A4"
]

companies = [
    "Maruti",
    "Hyundai",
    "Honda",
    "Toyota",
    "Mahindra",
    "BMW",
    "Audi"
]
fuel_types = ["Petrol", "Diesel", "LPG"]



name = st.selectbox("Car Name", car_names)
company = st.selectbox("Company", companies)
year = st.number_input("Year", min_value=1990,max_value=2025, value=2018,step=1)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=50000,
    step=1000
)
fuel_type = st.selectbox("Fuel Type", fuel_types)


# Prediction

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "name": [name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })
    prediction =model.predict(input_df)
    
    st.success(f"Estimated Car Price: ₹ {prediction[0]:,.2f}")