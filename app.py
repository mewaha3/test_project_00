import streamlit as st

def main():
    st.title("Job Management System")
    
    # Sidebar for Navigation
    menu = ["User Registration", "Employer - Post Job", "Employee - Apply for Job", "Process Payment", "Submit Review"]
    choice = st.sidebar.selectbox("Select Form", menu)
    
    if choice == "User Registration":
        st.subheader("User Registration Form")
        user_id = st.text_input("User ID")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        user_type = st.radio("User Type", ["Employee", "Employer"])
        
        if st.button("Register"):
            st.success(f"User {user_id} registered successfully as {user_type}!")
    
    elif choice == "Employer - Post Job":
        st.subheader("Post a Job")
        job_title = st.text_input("Job Title")
        job_desc = st.text_area("Job Description")
        salary = st.number_input("Salary", min_value=0.0, format="%.2f")
        max_retries = st.slider("Max Retries", 1, 5, 3)
        
        if st.button("Post Job"):
            st.success(f"Job '{job_title}' posted successfully!")
    
    elif choice == "Employee - Apply for Job":
        st.subheader("Apply for a Job")
        employee_id = st.text_input("Employee ID")
        skills = st.text_area("Skills (comma-separated)")
        job_id = st.text_input("Job ID to Apply")
        
        if st.button("Apply"):
            st.success(f"Employee {employee_id} applied for Job {job_id}!")
    
    elif choice == "Process Payment":
        st.subheader("Process Payment")
        job_id = st.text_input("Job ID")
        amount = st.number_input("Payment Amount", min_value=0.0, format="%.2f")
        payment_status = st.selectbox("Payment Status", ["Pending", "Processed", "Released"])
        
        if st.button("Submit Payment"):
            st.success(f"Payment for Job {job_id} updated to {payment_status}!")
    
    elif choice == "Submit Review":
        st.subheader("Submit Review")
        reviewer_id = st.text_input("Reviewer ID")
        reviewee_id = st.text_input("Employee/Employer ID")
        rating = st.slider("Rating", 1, 5, 3)
        comment = st.text_area("Comments")
        
        if st.button("Submit Review"):
            st.success(f"Review submitted for {reviewee_id} with rating {rating}!")
    
if __name__ == "__main__":
    main()
