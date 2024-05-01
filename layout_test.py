import streamlit as st

# adiciona uma selectbox na barra lateral
add_selectbox = st.sidebar.selectbox(
        'how would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')

)

# adiciona um slider na barra lateral
add_slider = st.sidebar.slider(
        'Select a range of values',
        0.9, 100.0, (25.0, 75.0
))
