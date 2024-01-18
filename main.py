import streamlit as st

# Carregar uma imagem localmente
imagem_local = "teste.png"
st.image(imagem_local, caption='Legenda da Imagem', use_column_width=True)

