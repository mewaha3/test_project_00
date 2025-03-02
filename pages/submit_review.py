import streamlit as st

def show():
    st.subheader("Submit Review")
    reviewer_id = st.text_input("Reviewer ID")
    reviewee_id = st.text_input("Employee/Employer ID")
    rating = st.slider("Rating", 1, 5, 3)
    comment = st.text_area("Comments")
    if st.button("Submit Review"):
        st.success(f"Review submitted for {reviewee_id} with rating {rating}!")
