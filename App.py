import streamlit as st
from intro_page import show as show_intro
from preProcess_page import show as show_preprocess
from EDA_page import show as show_eda
from styles import overall_css

# Set up app configuration and title - should be the first Streamlit command in your script
st.set_page_config(page_title="WeatherElectric Analytics", layout="wide")

# Inject custom CSS
st.markdown(overall_css, unsafe_allow_html=True)

# Main title
st.title('System Load Predictor App')

# Create a grid layout with three columns for the buttons
col1, col2, col3 = st.columns(3)

# Display buttons to select page in a row at the top of each page
with col1:
    intro_button = st.button("Introduction")
with col2:
    preprocess_button = st.button("PreProcessing")
with col3:
    eda_button = st.button("EDA")

# Get current page from session state
current_page = st.session_state.get("page", "intro")

# Update session state based on button clicks
if intro_button:
    current_page = "intro"
elif preprocess_button:
    current_page = "preprocess"
elif eda_button:
    current_page = "EDA"

# Save the current page to session state
st.session_state.page = current_page

# Page content based on current_page
if current_page == "intro":
    show_intro()
elif current_page == "preprocess":
    show_preprocess()
elif current_page == "EDA":
    show_eda()
