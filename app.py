import streamlit as st
import random
 
 
st.title('Tia Has been here')
st.write('Hello stranger!')
 

option = st.sidebar.selectbox(
    "Choose a section:",
    ["Home", "Page 1", "Page 2", "Page 3"]
)



if option == "Home":
    if st.button('Generate Random Number'):
        random_number = random.randint(1, 100)
        st.write(f'Random Number: {random_number}')
