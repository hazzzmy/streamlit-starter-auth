import streamlit as st
import time

from yaml.loader import SafeLoader
import yaml
import streamlit_authenticator as stauth

import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Radio Networks Analysis",
                   page_icon='data/favTBG.png', layout="wide")


if "auth" not in st.session_state:
    st.session_state["auth"] = False
if "role" not in st.session_state:
    st.session_state["role"] = None
if "login_name" not in st.session_state:
    st.session_state["login_name"] = None
if "login_username" not in st.session_state:
    st.session_state["login_username"] = None
if "authentication_status" not in st.session_state:
    st.session_state['authentication_status'] = None
if "isLogin" not in st.session_state:
    st.session_state["isLogin"] = False
if "authenticator" not in st.session_state:
    st.session_state["authenticator"] = None

# AUTHENTICATION
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.session_state['authenticator'] = authenticator

if st.session_state['auth'] == False:

    col1, col2 = st.columns(2)
    with col1:
        name, authentication_status, username = authenticator.login(
            "Radio Network Analytics Tools", "main")
        st.session_state['authentication_status'] = authentication_status
        st.session_state['login_name'] = name
        st.session_state['login_username'] = username

        success_message = st.empty()

        if st.session_state['authentication_status'] == False:
            st.error("Username or password is incorrect")
        elif st.session_state['authentication_status'] == None:
            st.warning("Please enter your username and password")
        elif st.session_state['authentication_status'] == True:

            success_message = st.success(
                'You have successfully logged in', icon="✅")
            time.sleep(1)
            success_message.empty()

            st.session_state['isLogin'] = True
            st.session_state['auth'] = True

    with col2:
        st.empty()

if st.session_state['authentication_status']:
    st.header("Halaman Home")
    st.info("You are logged in as " + st.session_state['login_name'])

if st.session_state['auth'] == True:

    colName, colButton = st.sidebar.columns(2)
    with colName:
        st.sidebar.info(st.session_state['login_name'])
    with colButton:
        logout = authenticator.logout("Logout", "sidebar")

        if st.session_state['authentication_status'] == None:
            st.session_state['auth'] = False
            st.session_state['isLogin'] = False

            message = st.sidebar.success(
                'You have logged out')
            time.sleep(1)
            message.empty()

hide_default_format = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_default_format, unsafe_allow_html=True)

make_map_responsive = """
<style>
[title~="st.iframe"] { width: 100%}
</style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
