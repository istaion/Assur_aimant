import streamlit as st 
st.title("ASSUR'AIMANT VOUS SOUHAITE LA BIENVENUE")

st.write('Bienvenu sur notre plateforme de simulation pour votre redevance, le principe est simple avec 4 différents modeles avec les données fournies par un utilisateur')

st.image('Hacene/image.jpg')

link_html = """
<div style="text-align: center;">
    <a href="prediction_client" target="_self" style="font-size:20px; text-decoration: none; color: #0073e6;">Débutez la simulation</a>
</div>
"""

# Affichage du lien centré
st.markdown(link_html, unsafe_allow_html=True)
