import streamlit as st
import json
import os

# ไฟล์เก็บข้อมูลผู้ใช้
USER_DATA_FILE = "users.json"

# ฟังก์ชันโหลดข้อมูลผู้ใช้
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# ฟังก์ชันบันทึกข้อมูลผู้ใช้
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login_page():
    st.title("🔐 Sign In / Sign Up Page")

    users = load_users()  # โหลดข้อมูลผู้ใช้จากไฟล์

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    menu = st.radio("Select an option", ["Sign In", "Sign Up"])

    if menu == "Sign Up":
        st.subheader("Create a new account")
        new_username = st.text_input("New Username", key="new_username")
        new_password = st.text_input("New Password", type="password", key="new_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

        if st.button("Sign Up"):
            if new_username in users:
                st.error("❌ Username already exists!")
            elif new_password != confirm_password:
                st.error("❌ Passwords do not match!")
            else:
                users[new_username] = new_password
                save_users(users)  # บันทึกข้อมูลผู้ใช้
                st.success("✅ Account created successfully! You can now sign in.")

    elif menu == "Sign In":
        st.subheader("Sign In to your account")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")

        if st.button("Sign In"):
            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("✅ Sign In successful!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password")

    if st.session_state.logged_in:
        st.success(f"Welcome, {st.session_state.username}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()

if __name__ == "__main__":
    login_page()
