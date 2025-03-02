import streamlit as st

def show():
    st.subheader("User Registration Form")
    user_id = st.text_input("User ID")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    user_type = st.radio("User Type", ["Employee", "Employer"])
    if st.button("Register"):
        st.success(f"User {user_id} registered successfully as {user_type}!")
