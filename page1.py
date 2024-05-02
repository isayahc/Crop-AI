import streamlit as st
from api import predict_tabular_classification_sample

def all_params() :
    st.title("Flexible Farming")
    st.subheader("Recommend crops for your current conditions")
    st.sidebar.success("Type of Data")
    st.sidebar.page_link("mainapp.py", label="Home")
    st.sidebar.page_link('pages/page1.py', label="Input All Fields")
    st.sidebar.page_link('pages/page2.py', label="Location as Field")
    Ncontent = st.text_input("Nitrogen in soil")
    Pcontent = st.text_input("Phosphorous in soil")
    Kcontent = st.text_input("Potassium in soil")
    temperature = st.text_input("Temperature (Celcius)")
    humidity = st.text_input("Humidity percentage")
    ph = st.text_input("ph of soil")
    rainfall = st.text_input("rainfall in mm")
    if st.button("Submit") :
        #call api here
        st.write("") 
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

    #location = st.text_input("Where are you?")
    #st.write(get_temp(location))
    #get_temp("Alpharetta")
    #get_humidity("Alpharetta")
    #print(f'{round(get_temp("Alpharetta"), 2)}    {get_humidity("Alpharetta")}')
st.set_page_config(page_title="All Fields", page_icon="📈")
all_params()
