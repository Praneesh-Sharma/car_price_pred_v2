#Importing libraries
import streamlit as st
import pandas as pd
import pickle

st.title('Car Price Prediction')

with open("car_price.sav", 'rb') as f:
   wine_pred_model = pickle.load(f)

col1, col2 = st.columns(2)

a = st.number_input("Present Price:",
                      min_value=0.20,
                      max_value=100.00,
                      step=1
      )

b = st.number_input("KMs driven",
                      min_value=50,
                      max_value=500000,
                      step=1
      )

c = st.selectbox("Fuel Type",
                   ("Petrol", "Diesel", "CNG),
                   index=None,
                   placeholder="Select fuel type...",
                  )
