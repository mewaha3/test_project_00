import streamlit as st

def main():
    st.title("Web Form for Job Management")
    
    # User Registration
    st.header("User Registration")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Select Role", ["Employee", "Employer"])
    
    if role == "Employee":
        st.header("Employee Section")
        skills = st.text_area("Enter Your Skills")
        looking_for_jobs = st.checkbox("Looking for Jobs?")
    
    elif role == "Employer":
        st.header("Employer Section")
        job_description = st.text_area("Job Description")
        salary_offer = st.number_input("Salary Offer ($)", min_value=0.0, step=100.0)
        num_positions = st.number_input("Number of Positions", min_value=1, step=1)
    
    # Job Matching Process
    st.header("Job Matching")
    match_jobs = st.button("Find Matching Jobs")
    
    if match_jobs and role == "Employee":
        st.success("Matching jobs found based on your skills!")
    elif match_jobs and role == "Employer":
        st.success("Top candidates found for your job posting!")
    
    # Payment Section
    st.header("Payment Process")
    if role == "Employer":
        confirm_payment = st.button("Confirm Payment to Employee")
        if confirm_payment:
            st.success("Payment Processed Successfully!")
    
    if role == "Employee":
        confirm_receipt = st.button("Confirm Receipt of Payment")
        if confirm_receipt:
            st.success("Payment Received!")
    
    # Job Review
    st.header("Job Review")
    if role == "Employer":
        review_employee = st.text_area("Review Employee Performance")
        submit_review = st.button("Submit Review")
        if submit_review:
            st.success("Employee review submitted!")
    
    if role == "Employee":
        review_job = st.text_area("Review Job Experience")
        submit_job_review = st.button("Submit Job Review")
        if submit_job_review:
            st.success("Job review submitted!")

if __name__ == "__main__":
    main()
