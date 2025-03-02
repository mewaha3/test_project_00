import streamlit as st

def login_page():
    st.title("🔐 Sign In / Sign Up Page")
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    menu = st.radio("Select an option", ["Sign In", "Sign Up"])
    
    if menu == "Sign Up":
        st.subheader("Create a new account")
        new_username = st.text_input("New Username", key="new_username")
        new_password = st.text_input("New Password", type="password", key="new_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        
        if st.button("Sign Up"):
            if new_password == confirm_password:
                st.session_state[new_username] = new_password
                st.success("✅ Account created successfully! You can now sign in.")
            else:
                st.error("❌ Passwords do not match!")
    
    elif menu == "Sign In":
        st.subheader("Sign In to your account")
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        if st.button("Sign In"):
            if username in st.session_state and st.session_state[username] == password:
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
