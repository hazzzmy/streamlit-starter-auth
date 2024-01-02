import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import geopandas as gpd

from module.helper import logout, redirectButton

import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Page Example",
                   page_icon='data/favTBG.png', layout="wide")

if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if st.session_state['auth'] == True:
    logout(st.session_state['authenticator'])

if st.session_state['auth'] == False:
    st.info(
        'Please regenerate authentication with revisit the Home Page, then come back to this page')
    urlHome = "http://localhost:8501"
    goToHome = redirectButton("Go To Home Page", urlHome)
    goToHomeButton = goToHome

else:
    st.header('Page Example')
