import streamlit as st
from database import get_user

st.title("Login Page")

username = st.text_input("Enter Username")
password = st.text_input("Enter Password", type="password")

login = st.button("Login")

if login:

    user = get_user(username)

    if user is None:
        st.error("Username does not exist.")

    elif user[2] != password:
        st.error("Incorrect Password.")

    else:
        st.session_state["username"] = username
        st.switch_page("pages/3_welcome.py")

    



