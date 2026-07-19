import streamlit as st
from database import delete_user, check_username

st.title("Delete Account")

username = st.text_input("Enter Username")

if "confirm_delete" not in st.session_state:
    st.session_state.confirm_delete = False

if st.button("Delete Account"):
    if not check_username(username):
        st.error("Username does not exist.")
    else:
        st.session_state.confirm_delete = True

if st.session_state.confirm_delete:
    st.warning("Are you sure you want to delete your account?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes"):
            delete_user(username)
            st.success("Account Deleted Successfully")
            st.session_state.confirm_delete = False

    with col2:
        if st.button("No"):
            st.info("Account Deletion Cancelled")
            st.session_state.confirm_delete = False