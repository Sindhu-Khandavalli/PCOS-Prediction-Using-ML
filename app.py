import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="PCOS Prediction",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 PCOS Prediction System")
st.write("Enter the patient details below to predict PCOS.")

# -----------------------------
# Load model
# -----------------------------
with open("logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input(
    "Age",
    min_value=18,
    max_value=45,
    value=25
)

bmi = st.number_input(
    "BMI",
    min_value=18.0,
    max_value=35.0,
    value=24.0
)

menstrual_irregularity = st.selectbox(
    "Menstrual Irregularity",
    ["No", "Yes"]
)

testosterone = st.number_input(
    "Testosterone Level (ng/dL)",
    min_value=20.0,
    max_value=100.0,
    value=50.0
)

antral_follicle_count = st.number_input(
    "Antral Follicle Count",
    min_value=5,
    max_value=30,
    value=15
)

# Convert Yes/No to 0/1
menstrual_value = 1 if menstrual_irregularity == "Yes" else 0

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict PCOS"):

    input_data = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Menstrual_Irregularity": [menstrual_value],
        "Testosterone_Level(ng/dL)": [testosterone],
        "Antral_Follicle_Count": [antral_follicle_count]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ PCOS Prediction: Positive")
    else:
        st.success("✅ PCOS Prediction: Negative")