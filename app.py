import streamlit as st

def user_registration():
    st.subheader("User Registration Form")
    user_id = st.text_input("User ID")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    user_type = st.radio("User Type", ["Employee", "Employer"])
    
    if st.button("Register"):
        st.session_state['registered_user'] = {
            'user_id': user_id,
            'email': email,
            'user_type': user_type
        }
        st.success(f"User {user_id} registered successfully as {user_type}!")
        st.switch_page("Employer - Post Job")

def post_job():
    st.subheader("Post a Job")
    job_title = st.text_input("Job Title")
    job_desc = st.text_area("Job Description")
    salary = st.number_input("Salary", min_value=0.0, format="%.2f")
    max_retries = st.slider("Max Retries", 1, 5, 3)
    
    if st.button("Post Job"):
        st.success(f"Job '{job_title}' posted successfully!")

def apply_job():
    st.subheader("Apply for a Job")
    employee_id = st.text_input("Employee ID")
    skills = st.text_area("Skills (comma-separated)")
    job_id = st.text_input("Job ID to Apply")
    
    if st.button("Apply"):
        st.success(f"Employee {employee_id} applied for Job {job_id}!")

def process_payment():
    st.subheader("Process Payment")
    job_id = st.text_input("Job ID")
    amount = st.number_input("Payment Amount", min_value=0.0, format="%.2f")
    payment_status = st.selectbox("Payment Status", ["Pending", "Processed", "Released"])
    
    if st.button("Submit Payment"):
        st.success(f"Payment for Job {job_id} updated to {payment_status}!")

def submit_review():
    st.subheader("Submit Review")
    reviewer_id = st.text_input("Reviewer ID")
    reviewee_id = st.text_input("Employee/Employer ID")
    rating = st.slider("Rating", 1, 5, 3)
    comment = st.text_area("Comments")
    
    if st.button("Submit Review"):
        st.success(f"Review submitted for {reviewee_id} with rating {rating}!")

def main():
    st.title("Job Management System")
    
    # Sidebar Navigation
    menu = {
        "User Registration": user_registration,
        "Employer - Post Job": post_job,
        "Employee - Apply for Job": apply_job,
        "Process Payment": process_payment,
        "Submit Review": submit_review
    }
    choice = st.sidebar.radio("Select Page", list(menu.keys()))
    
    # Navigate to selected page
    menu[choice]()
    
if __name__ == "__main__":
    main()
