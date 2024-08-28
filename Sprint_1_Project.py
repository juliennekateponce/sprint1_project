import streamlit as st
import pandas as pd

st.title("Mapping MooLAH :dollar:")
st.subheader("Uncovering Spending Patterns and Customer Segments for Targeted Marketing")
st.write("Sprint 1 Project ｜ Group 5 - Sinigang")
st.image("slides/2.jpg")
st.image("slides/3.jpg")

st.sidebar.image("slides/icon.png", caption="icon", use_column_width=True)
st.sidebar.image("slides/mapping_moolah.png", caption="mapping_moolah", use_column_width=True)

def background():

    # Load photo
    st.title("Data Background")
    # st.write("Provide a short description of the problem and your objective.")
    st.image("slides/5.jpg")
    st.image("slides/6.jpg")
    st.image("slides/7.jpg")
    st.image("slides/8.jpg")
    st.image("slides/9.jpg")
    st.image("slides/11.jpg")

def preprocessing():
    st.title("Data Preprocessing")
    st.image("slides/12.jpg")
    st.image("slides/13.jpg")

def eda():
    st.title("EDA")
    st.image("slides/14.jpg")
    st.image("slides/15.jpg")
    st.image("slides/16.jpg")
    st.image("slides/17.jpg")

def modeling():
    st.title("Modeling")
    st.image("slides/19.jpg")
    st.image("slides/20.jpg")
    st.image("slides/21.jpg")
    st.image("slides/22.jpg")
    st.image("slides/23.jpg")
    st.image("slides/24.jpg")
    st.image("slides/25.jpg")
    st.image("slides/26.jpg")
    st.image("slides/27.jpg")

def findings():
    st.title("Findings")
    st.image("slides/29.jpg")
    st.image("slides/30.jpg")
    

list_of_pages = [
    "Data Background",
    "Data Preprocessing",
    "EDA",
    "Modeling",
    "Findings"
]

st.sidebar.title(':dollar: Mapping MooLAH')
selection = st.sidebar.radio("Content", list_of_pages)

if selection == "Data Background":
    background()

elif selection == "Data Preprocessing":
    preprocessing()

elif selection == "EDA":
    eda()

elif selection == "Modeling":
    modeling()

elif selection == "Findings":
    findings()
