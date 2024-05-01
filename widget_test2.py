import streamlit as st
st.text_input("Your name", key="name")

# é possível acessar o valor a qualquer hora com:
st.session_state.name
