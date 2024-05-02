import streamlit as st
from locationStats import get_temp
from locationStats import get_humidity
from api import predict_tabular_classification_sample


def location_params() :
    st.title("Flexible Farmers")
    st.subheader("Recommend crops for your current conditions")
    st.sidebar.success("Type of Data")
    st.sidebar.page_link("mainapp.py", label="Home")
    st.sidebar.page_link('pages/page1.py', label="Input All Fields")
    st.sidebar.page_link('pages/page2.py', label="Location as Field")
    location = st.text_input("Enter your location")
    
    Ncontent = st.text_input("Nitrogen in soil")
    Pcontent = st.text_input("Phosphorous in soil")
    Kcontent = st.text_input("Potassium in soil")
    ph = st.text_input("ph of soil")
    rainfall = st.text_input("rainfall in mm")
    if st.button("Submit") :
        humidity = get_humidity(location)
        temperature = get_temp(location)
        temperature = round(temperature, 2)
        data = predict_tabular_classification_sample(instance_dict={
            "N":Ncontent,
            "P":Pcontent,
            "K":Kcontent,
            "temperature": temperature,
            "humidity": humidity,
            "ph":ph,
            "rainfall": rainfall,
        })
        st.write(f'The best crop for your condition is: {data}')

    #submission

st.set_page_config(page_title="Location as Field", page_icon="📈")
location_params()