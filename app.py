# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N-sXGc6QQ8lsgBiGGBnd7FSqfSnwb-l1
"""

import streamlit as st
import random

st.title('Wiritphon Yusamran')
st.write('Hello Mew!')

if st.button('Generate Random Number'):
    random_number = random.randint(1, 100)
    st.write(f'Random Number: {random_number}')
