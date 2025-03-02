import streamlit as st
import sqlite3
import pandas as pd

# Database connection
conn = sqlite3.connect('job_matching.db', check_same_thread=False)
c = conn.cursor()

# Create tables if not exist
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, role TEXT, skills TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, employer TEXT, description TEXT, skills_required TEXT, status TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY, job_id INTEGER, employee TEXT, status TEXT)''')
conn.commit()

# User authentication
st.sidebar.title("Job Matching System")
page = st.sidebar.radio("Navigation", ["Register", "Login", "Find Job", "Manage Jobs", "Payments"])

if page == "Register":
    st.title("User Registration")
    username = st.text_input("Username")
    role = st.selectbox("Role", ["Employer", "Employee"])
    skills = st.text_area("Skills (comma separated)")
    if st.button("Register"):
        c.execute("INSERT INTO users (username, role, skills) VALUES (?, ?, ?)", (username, role, skills))
        conn.commit()
        st.success("Registered Successfully! Please Login.")

elif page == "Login":
    st.title("Login")
    username = st.text_input("Username")
    if st.button("Login"):
        user = c.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        if user:
            st.session_state["user"] = user
            st.success(f"Welcome {username}!")
        else:
            st.error("User not found")

elif page == "Find Job" and "user" in st.session_state:
    st.title("Find Jobs")
    user = st.session_state["user"]
    if user[2] == "Employee":
        jobs = pd.read_sql("SELECT * FROM jobs WHERE status='Open'", conn)
        st.write(jobs)
        selected_job = st.selectbox("Select a job", jobs["id"] if not jobs.empty else [])
        if st.button("Apply"):
            c.execute("UPDATE jobs SET status='Pending' WHERE id=?", (selected_job,))
            conn.commit()
            st.success("Applied Successfully!")
    else:
        st.error("Only Employees can find jobs")

elif page == "Manage Jobs" and "user" in st.session_state:
    st.title("Manage Jobs")
    user = st.session_state["user"]
    if user[2] == "Employer":
        description = st.text_area("Job Description")
        skills_required = st.text_area("Required Skills")
        if st.button("Post Job"):
            c.execute("INSERT INTO jobs (employer, description, skills_required, status) VALUES (?, ?, ?, 'Open')", (user[1], description, skills_required))
            conn.commit()
            st.success("Job Posted Successfully!")
    else:
        st.error("Only Employers can manage jobs")

elif page == "Payments" and "user" in st.session_state:
    st.title("Payments")
    payments = pd.read_sql("SELECT * FROM payments", conn)
    st.write(payments)

st.sidebar.text("Made with Streamlit")
