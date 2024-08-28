import streamlit as st
import pandas as pd

st.title("Mapping MooLAH")
st.write("Uncovering Spending Patterns and Customer Segments for Targeted Marketing")
st.write("Group 5 - Sinigang")


def introduction():

    # Load photo
    st.title("Introduction")
    # st.write("Provide a short description of the problem and your objective.")
    st.image("")

def fi_state_ph():
    st.title("Methodology")
    st.image("")
    
def fi_state_worldwide():
    st.title("Conclusions")
    st.image("")

def recommendations():
    st.title("Recommendations")
    st.image("")

def the_team():
    st.title("") 
    st.image("")


list_of_pages = [
    "Introduction",
    "Methodology",
    "Conclusions",
    "Recommendations",
    ""
]

st.sidebar.title(':dollar: Mapping MooLAH')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Methodology":
    fi_state_ph()

elif selection == "Conclusions":
    fi_state_worldwide()

elif selection == "Recommendations":
    recommendations()

elif selection == "":
    the_team()
