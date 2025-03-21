import streamlit as st
import pandas as pd
import numpy as np
from modules.orchestrator import get_patient, predict_charges
from modules.logger import logger
import altair as alt
import io

st.set_page_config(page_title="Projet 3", page_icon="🧊", layout="wide")

st.title("Projet 3")

st.header("1. Récupérer la liste des patients(api-projet1)")

if st.button("Charger la liste des patients"):
    api_projet1 = "http://api-projet1:8000"
    patients = get_patient(api_projet1)
    if patients is not None:
        st.write(patients)
    else:
        st.error("Erreur lors de la récupération des patients")

st.header("2. Prédire le coût de l'assurance d'un patient(api-projet2)")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", min_value=0, max_value=100, value=30, step=1)
    bmi = st.slider("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

with col2:
    sexe = st.selectbox("Sexe", ["male", "female"])
    smoker = st.selectbox("Fumeur", ["yes", "no"])

with col3:
    children = st.number_input("Nombre d'enfants", min_value=0, max_value=10, value=0, step=1)
    region = st.selectbox("Région", ["southwest", "southeast", "northwest", "northeast"])

if st.button("Prédire le coût de l'assurance"):
    api_projet2 = "http://api-projet2:8000"
    prediction = predict_charges(
        api_projet2, 
        age=age, 
        bmi=bmi, 
        children=children, 
        sexe=sexe, 
        smoker=smoker, 
        region=region
    )
    if prediction is not None:
        st.success(f"Le coût de l'asssurance est de : {prediction:.2f}")
    else:
        st.error("Erreur lors de la prédiction du coût de l'assurance")

st.write("log récent : voir le fichier log pour plus de détails")
logger.info("log récent pour l'application streamlit")
