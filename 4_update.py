import streamlit as st
import re
from database import update_user, check_username

st.title("Update Account")

if "updated" not in st.session_state:
    st.session_state.updated = False

old_username = st.text_input("Current Username")
new_username = st.text_input("New Username")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Update"):

    if len(new_username) < 5:
        st.error("Username must be at least 5 characters.")

    elif old_username != new_username and check_username(new_username):
        st.error("Username already exists.")

    elif new_password != confirm_password:
        st.error("Passwords do not match.")

    elif len(new_password) < 8:
        st.error("Password must be at least 8 characters.")

    elif not re.search("[A-Z]", new_password):
        st.error("Password must contain at least one uppercase letter.")

    elif not re.search("[a-z]", new_password):
        st.error("Password must contain at least one lowercase letter.")

    elif not re.search("[0-9]", new_password):
        st.error("Password must contain at least one digit.")

    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", new_password):
        st.error("Password must contain at least one special character.")

    else:
        update_user(old_username, new_username, new_password)
        st.success("Account Updated Successfully")
        st.session_state.updated = True

if st.session_state.updated:
    if st.button("Back to Welcome"):
        st.session_state.updated = False
        st.switch_page("pages/3_welcome.py")