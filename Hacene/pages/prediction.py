import streamlit as st
import pandas as pd
from donnees import df_2, line_reg
st.title("Prédiction de la redevance du client")

# with st.form('manipuler les membres', clear_on_submit= True):

age = st.text_input('quel est votre age?')


if age != "":
    if age.isdigit():
        age = int(age)
    else:
        st.error("L'âge doit être un nombre entier.")
else:
    age = None  


poids = st.text_input('quel est votre poids en kilos?')

if poids != "":
    if poids.isdigit():
        poids = int(poids)
    else:
        st.error("le poids doit être un nombre entier.")
else:
    poids = None




taille = st.text_input('quel est votre taille en cm?')

if taille != "":
    if taille.isdigit():
        taille = int(taille)
    else:
        st.error("le taille doit être un nombre entier.")
else:
    taille = None  




nb_enfant = int(st.radio("combien d'enfants",[0,1,2,3,4,5]))
sexe = st.radio('êtes-vous un homme ou une femme', ('Homme','Femme'))
fumeur = st.radio('Fumez-vous?',('oui','non'))
region = st.selectbox('de quel region venez vous ?', ['northeast', 'northwest', 'southest','southwest'])

# liste des différentes catégories de poids
imc = int(poids) / ((int(taille) /100) ** 2)


if imc <= 18.5:
    imc_cat = [1,0,0,0,0]
elif imc >18.5 and imc <= 25:
    imc_cat = [0,1,0,0,0]
elif imc >25 and imc <= 30:
    imc_cat = [0,0,1,0,0]
elif imc >30 and imc <= 40:
    imc_cat = [0,0,0,1,0]
elif imc > 40:
    imc_cat = [0,0,0,0,1]

# categorie sexe

if sexe == 'Homme':
    cat_sexe = 0
else:
    cat_sexe = 1

# categorie fumeur

if fumeur == 'non':
    cat_fumeur = 0
else:
    cat_fumeur = 1


#categorie region

if region == 'northeast':
    cat_region = [1,0,0,0]
if region == 'northwest':
    cat_region = [0,1,0,0]
if region == 'southeast':
    cat_region = [0,0,1,0]
if region == 'southwest':
    cat_region = [0,0,0,1]

    # ajouter_un_membre = st.form_submit_button('ajouter membre')

test_personne = [age,nb_enfant,cat_sexe,cat_fumeur]
for element in cat_region:
    test_personne.append(element)
for element in imc_cat:
    test_personne.append(element)

nom_colonnes = df_2.drop(['charges', 'bmi'],axis = 1).columns


df_test = pd.DataFrame([test_personne], columns=nom_colonnes)

st.write(df_test)

