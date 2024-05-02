import streamlit as st
import pandas as pd
import streamlit.components.v1 as components;
from dotenv import load_dotenv
load_dotenv()

submitted = False
st.title("Flexible Farmers")
st.subheader("Find out what crops/plants to grow.")
Ncontent = 90
Ncontent = st.number_input("Nitrogen in soil")
Pcontent = 42
Pcontent = st.number_input("Phosphorous in soil")
Kcontent = 43
Kcontent = st.number_input("Potassium in soil")
temperature = 20.88
temperature = st.number_input("Temperature (Celcius)")
humidity = 82
humidity = st.number_input("Humidity percentage")
ph = 6.5
ph = st.number_input("ph of soil")
rainfall = 202.9
rainfall = st.number_input("rainfall in mm")
if st.button("Submit") :
    #call api here
    st.write("")
