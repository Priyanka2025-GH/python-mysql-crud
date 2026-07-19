
import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

st.title("User Management System")

option = st.radio(
    "Choose an option",
    ["Signup", "Login"]
)

if option == "Signup":
    st.switch_page("pages/1_sign.py")

if option == "Login":
    st.switch_page("pages/2_login.py")