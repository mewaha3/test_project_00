import streamlit as st

def show():
    st.subheader("Post a Job")
    job_title = st.text_input("Job Title")
    job_desc = st.text_area("Job Description")
    salary = st.number_input("Salary", min_value=0.0, format="%.2f")
    max_retries = st.slider("Max Retries", 1, 5, 3)
    if st.button("Post Job"):
        st.success(f"Job '{job_title}' posted successfully!")
