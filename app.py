import streamlit as st
from pages import user_registration, employer_post_job, employee_apply_job, process_payment, submit_review

def main():
    st.title("Job Management System")
    
    # Sidebar Navigation
    menu = {
        "User Registration": user_registration.show,
        "Employer - Post Job": employer_post_job.show,
        "Employee - Apply for Job": employee_apply_job.show,
        "Process Payment": process_payment.show,
        "Submit Review": submit_review.show
    }
    choice = st.sidebar.radio("Select Page", list(menu.keys()))
    
    # Navigate to selected page
    menu[choice]()
    
if __name__ == "__main__":
    main()
