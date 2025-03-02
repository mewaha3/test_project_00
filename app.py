import streamlit as st

def register():
    st.title("Job Management System")
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
        st.session_state['page'] = 'post_job'

def post_job():
    st.title("Employer - Post Job")
    st.subheader("Post a Job")
    job_title = st.text_input("Job Title")
    job_desc = st.text_area("Job Description")
    salary = st.number_input("Salary", min_value=0.0, format="%.2f")
    max_retries = st.slider("Max Retries", 1, 5, 3)
    
    if st.button("Post Job"):
        st.session_state['job_posted'] = {
            'job_title': job_title,
            'job_desc': job_desc,
            'salary': salary,
            'max_retries': max_retries
        }
        st.success(f"Job '{job_title}' posted successfully!")
        st.session_state['page'] = 'apply_job'

def apply_job():
    st.title("Employee - Apply for Job")
    st.subheader("Apply for a Job")
    employee_id = st.text_input("Employee ID")
    skills = st.text_area("Skills (comma-separated)")
    job_id = st.text_input("Job ID to Apply")
    
    if st.button("Apply"):
        st.session_state['job_application'] = {
            'employee_id': employee_id,
            'skills': skills,
            'job_id': job_id
        }
        st.success(f"Employee {employee_id} applied for Job {job_id}!")
        st.session_state['page'] = 'matching'

def matching():
    st.title("Matching Employees with Employers")
    st.subheader("Matching System")
    
    if 'registered_user' in st.session_state and 'job_posted' in st.session_state and 'job_application' in st.session_state:
        st.write("### Job Details:")
        st.json(st.session_state['job_posted'])
        
        st.write("### Applied Employee:")
        st.json(st.session_state['job_application'])
        
        st.success("Matching Completed!")
    else:
        st.warning("Incomplete data. Please ensure all steps are completed.")

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'register'
    
    if st.session_state['page'] == 'register':
        register()
    elif st.session_state['page'] == 'post_job':
        post_job()
    elif st.session_state['page'] == 'apply_job':
        apply_job()
    elif st.session_state['page'] == 'matching':
        matching()

if __name__ == "__main__":
    main()
