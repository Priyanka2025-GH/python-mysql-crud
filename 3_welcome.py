import streamlit as st

st.title("Welcome Page")

st.success("Login Successful")

st.write("Welcome", st.session_state.get("username", "User"))

if st.button("Update Account"):
    st.switch_page("pages/4_update.py")

if st.button("Delete Account"):
    st.switch_page("pages/5_delete.py")

if st.button("Logout"):
    st.switch_page("pages/2_login.py")