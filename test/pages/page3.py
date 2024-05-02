import streamlit as st
from locationStats import get_humidity
from locationStats import get_temp
def biotech() :
    st.header("Biotech🧬🌱")
    st.subheader("We wil create for you a yeast that will create a protein that will reconstitute the soil in your local environment")
    st.sidebar.page_link("mainapp.py", label="Home")
    st.sidebar.page_link('pages/page1.py', label="Input All Fields")
    st.sidebar.page_link('pages/page2.py', label="Location as Field")
    Ncontent = st.text_input("Nitrogen in soil")
    Pcontent = st.text_input("Phosphorous in soil")
    Kcontent = st.text_input("Potassium in soil")
    ph = st.text_input("ph of soil")
    language = st.text_input("Language")
    
    
