import streamlit as st
import time

'starting a long computation....'

# adicionando um placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    # atualizar a barra de progresso a cada iteração
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.10)

"...and now we/'re done"
