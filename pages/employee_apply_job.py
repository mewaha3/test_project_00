import streamlit as st

def show():
    st.subheader("Apply for a Job")
    employee_id = st.text_input("Employee ID")
    skills = st.text_area("Skills (comma-separated)")
    job_id = st.text_input("Job ID to Apply")
    if st.button("Apply"):
        st.success(f"Employee {employee_id} applied for Job {job_id}!")
