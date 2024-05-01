import streamlit as st

left_column, right_column = st.columns(2)

# da pra usar a coluna exatamente como na barra lateral

left_column.button('Press me!')

# ou melhor, chamar funções streamlit dentro de um bloco with

with right_column:
    chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
