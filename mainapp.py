import streamlit as st

st.set_page_config(
    page_title="Flexible Farming",
    page_icon="👋",
)
st.header("Flexible Farming!")
st.sidebar.success("Type of Data")
st.sidebar.page_link("mainapp.py", label="Home")
st.sidebar.page_link('pages/page1.py', label="Input All Fields")
st.sidebar.page_link('pages/page2.py', label="Location as Field")
st.sidebar.page_link('pages/page3.py', label="Biotech")
def run() :
    st.markdown(""" 
                Flexible Farming is an application that\'s purpose is to help farmers grow 
                crops that will be best for their environment """)

if __name__ == "__main__":
    run()