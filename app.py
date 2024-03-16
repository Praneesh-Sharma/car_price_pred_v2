#Importing libraries
import streamlit as st
import pandas as pd
import pickle

st.title('Car Price Prediction')

with open("car_price.sav", 'rb') as f:
   wine_pred_model = pickle.load(f)

col1, col2 = st.columns(2)


with col1:
   a = st.number_input("Present Price:")

with col2:
   b = st.number_input("KMs driven")

with col1:
   c = st.selectbox("Fuel Type",
                   ("Petrol", "Diesel", "CNG"),
                   index=None,
                   placeholder="Select fuel type...",
                  )
