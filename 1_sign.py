import streamlit as st
import re
from database import check_username,insert_user

st.title("Signup Page")

username = st.text_input("Enter Username")

password = st.text_input("Enter Password", type="password")

confirm_password = st.text_input("Confirm Password", type="password")

signup = st.button("Signup")


if signup:

    if len(username) < 5:
        st.error("Username must be at least 5 characters.")

    elif check_username(username):
        st.error("Username already exists.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    elif len(password) < 8:
        st.error("Password must be at least 8 characters.")

    elif not re.search("[A-Z]", password):
        st.error("Password must contain at least one uppercase letter.")

    elif not re.search("[a-z]", password):
        st.error("Password must contain at least one lowercase letter.")

    elif not re.search("[0-9]", password):
        st.error("Password must contain at least one digit.")

    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        st.error("Password must contain at least one special character.")

    else:
        insert_user(username, password)
        st.success("Signup Successful")

if st.button("Go to Login"):
    st.switch_page("pages/2_login.py")
    

