import streamlit as st
import time
def logout(authenticator):

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


def redirectButton(text, href):
    # Define CSS styles
    button_style = """
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
        border-radius: 2px;
    """
    return st.markdown(f'<a style="{button_style}" href="{href}" target="_self">{text}</a>', unsafe_allow_html=True)
