import streamlit as st

def show():
    st.subheader("Process Payment")
    job_id = st.text_input("Job ID")
    amount = st.number_input("Payment Amount", min_value=0.0, format="%.2f")
    payment_status = st.selectbox("Payment Status", ["Pending", "Processed", "Released"])
    if st.button("Submit Payment"):
        st.success(f"Payment for Job {job_id} updated to {payment_status}!")
