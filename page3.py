import streamlit as st
from locationStats import get_humidity
from locationStats import get_temp
import requests
from typing import Dict

def send_query(query_string: str) -> Dict[str, str]:
    url = 'https://1104-174-196-135-34.ngrok-free.app/query'
    headers = {'Content-Type': 'application/json'}
    data = {'query_string': query_string}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        return {'error': 'Failed to send query'}
    
def biotech() :
    st.header("Biotech🧬🌱")
    st.subheader("We wil create for you a yeast that will create a protein that will reconstitute the soil in your local environment")
    st.sidebar.page_link("mainapp.py", label="Home")
    st.sidebar.page_link('pages/page1.py', label="Input All Fields")
    st.sidebar.page_link('pages/page2.py', label="Location as Field")
    st.sidebar.page_link('pages/page3.py', label="Biotech")
    Ncontent = st.text_input("Nitrogen in soil", value=0)
    Pcontent = st.text_input("Phosphorous in soil", value=0)
    Kcontent = st.text_input("Potassium in soil", value=0)
    ph = st.text_input("ph of soil", value=0)
    language = st.text_input("Language", value="English")
    if st.button("Submit") :
    #call api here
        data = {
            "N":Ncontent,
            "P":Pcontent,
            "K":Kcontent,
            "ph":ph,
            "language" :language,
        }
        query_build = f"answer the user in {data['language']}. In my location the concentration of Nitrogen is {data['N']} the concentration of \
            Phosphorus is {data['P']}, the contration of potssium is {data['K']} , the ph level is {data['ph']}\
        .I am looking for a gene that can be used for baker's yeast to prevent or even reconstitute the soil from drought. "
    
        st.write(send_query(send_query))
    
    
    
st.set_page_config(page_title="Location as Field", page_icon="🧬")
st.markdown("# Gene recommender")
biotech()