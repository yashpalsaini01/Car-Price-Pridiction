
import streamlit as st
import pickle
import pandas as pd

with open("car.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details below to predict its selling price.")


car_names = [
    "Hyundai Santro Xing",
    "Mahindra Jeep CL550",
    "Hyundai Grand i10",
    "Ford EcoSport Titanium",
    "Ford Figo",
    "Hyundai Eon",
    'AFord EcoSport Ambiente',
    'Skoda Fabia Classic', 'Maruti Suzuki Stingray',
    'Hyundai Elite i20', 'Mahindra Scorpio SLE', 'Audi A8', 'Audi Q7',
    'Mahindra Scorpio S10', 'Hyundai i20 Sportz', 'Maruti Suzuki Vitara', 'Mahindra Bolero DI',
    'Maruti Suzuki Swift', 'Maruti Suzuki Wagon', 'Toyota Innova 2.0',
    'Renault Lodgy 85', 'Skoda Yeti Ambition', 'Maruti Suzuki Baleno',
    'Renault Duster 110', 'Renault Duster 85', 'Honda City 1.5',
    'Maruti Suzuki Dzire', 'Honda Amaze', 'Honda Amaze 1.5',
    'Chevrolet Beat LT', 'BMW 7 Series', 'Mahindra XUV500 W8',
    'Hyundai i10 Magna', 'Hyundai Verna Fluidic',
    'Maruti Suzuki Ertiga', 'Honda Amaze 1.2', 'Hyundai i20 Asta',
    'Maruti Suzuki Eeco', 'Maruti Suzuki Esteem', 'Maruti Suzuki Ritz',
    'Toyota Etios Liva', 'Chevrolet Spark', 'Nissan Micra XV',
    'Chevrolet Beat', 'Ford EcoSport Trend', 'Tata Indica V2',
    'Hindustan Motors Ambassador', 'Toyota Innova 2.5',
    'Volkswagen Jetta Highline', 'Volkswagen Polo Comfortline',
    'Volkswagen Polo', 'Mahindra Scorpio', 'Nissan Sunny',
    'Renault Kwid', 'Chevrolet Spark LT', 'Fiat Punto Emotion',
    'Hyundai i10 Sportz', 'Chevrolet Beat LS', 'Tata Indigo CS',
    'Hyundai Eon Era', 'Mahindra XUV500', 'Ford Fiesta', 'Hyundai i20'
]

companies = [
  'Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
    'Renault', 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen',
    'Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',
    'Mercedes', 'Land', 'Jaguar', 'Jeep', 'Volvo'
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