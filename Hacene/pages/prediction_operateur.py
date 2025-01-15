import streamlit as st
import pickle
from donnees import df_2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from model import AgeTransformer, BmiTransformer
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.metrics import mean_squared_error, root_mean_squared_error
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV, cross_validate
import matplotlib.pyplot as plt




st.title("Prédiction de la redevance du client")

# # Initialization
if 'showform' not in st.session_state:
    st.session_state['showform'] = 1
    st.session_state.test_personne = 0
    st.session_state.test_personne_2 = 0
    st.session_state.nom_colonnes = 0
    st.session_state.liste_pred = 0
    st.session_state.imc = 0

if st.session_state.showform :



    with st.form('manipuler les membres', clear_on_submit= True):

        int_poids = 0
        int_taille = 0
        imc_cat = []
        cat_region = []

        age = st.text_input('quel est votre age?')



        if age != "":
            if age.isdigit():
                age = int(age)
                age_int = int(age)
            else:
                st.error("L'âge doit être un nombre entier ou supérieur et égale à 18.")
        else:
            age = None  


        poids = st.text_input('quel est votre poids en kilos?')



        if poids != "":
            if poids.isdigit():
                poids = int(poids)
                int_poids = int(poids) 
            else:
                st.error("le poids doit être un nombre entier.")
                
        else:
            poids = None





        taille = st.text_input('quel est votre taille en cm?')

        if taille != "":
            if taille.isdigit():
                taille = int(taille)
                int_taille = int(taille)
            else:
                st.error("le taille doit être un nombre entier.")
        else:
            taille = None  


        if int_poids > 0 and int_taille > 0 and int_poids != '' and int_taille !='' :
            st.session_state.imc = int_poids / ((int_taille /100) ** 2)

            if st.session_state.imc<= 18.5:
                imc_cat = [1,0,0,0,0]
            elif st.session_state.imc>18.5 and st.session_state.imc<= 25:
                imc_cat = [0,1,0,0,0]
            elif st.session_state.imc>25 and st.session_state.imc<= 30:
                imc_cat = [0,0,1,0,0]
            elif st.session_state.imc>30 and st.session_state.imc<= 40:
                imc_cat = [0,0,0,1,0]
            elif st.session_state.imc> 40:
                imc_cat = [0,0,0,0,1]

        nb_enfant = int(st.radio("combien d'enfants",[0,1,2,3,4,5]))
        sexe = st.radio('êtes-vous un homme ou une femme', ('Homme','Femme'))
        fumeur = st.radio('Fumez-vous?',('oui','non'))
        region = st.pills('de quel region venez vous ?', ['northeast', 'northwest', 'southeast','southwest'])

        # liste des différentes catégories de poids


        # categorie sexe

        if sexe != "":
            if sexe == 'Homme':
                cat_sexe = 0
            else:
                cat_sexe = 1

        # categorie fumeur

        if fumeur != '':
            if fumeur == 'non':
                cat_fumeur = 0
            else:
                cat_fumeur = 1
        


        #categorie region

        if region != '':
            if region == 'northeast':
                cat_region = [1,0,0,0]
            if region == 'northwest':
                cat_region = [0,1,0,0]
            if region == 'southeast':
                cat_region = [0,0,1,0]
            if region == 'southwest':
                cat_region = [0,0,0,1]



        st.session_state.test_personne = [age,nb_enfant,cat_sexe,cat_fumeur]
        for element in cat_region:
            st.session_state.test_personne.append(element)
        for element in imc_cat:
            st.session_state.test_personne.append(element)

        st.session_state.nom_colonnes = df_2.drop(['charges', 'bmi'],axis = 1).columns

        # format du df pour le meilleur modele Lasso afin d'intégrer la pipeline

        if sexe == 'homme':
            sexe = 'male'
        else:
            sexe = 'female'

        if fumeur == 'oui':
            fumeur = 'yes'
        else:
            fumeur = 'no'


        st.session_state.test_personne_2 = [age,sexe,st.session_state.imc,nb_enfant,fumeur,region]



        if st.form_submit_button(' évaluez votre redevance') :
            st.session_state.showform = 0
            st.rerun()
        
else:

    with st.container():
        st.subheader("PROPOSEZ UN PRIX AUX CLIENTS LE PLUS ELEVE POSSIBLE")

# OUVERTURE DES MODELES AU FORMAT PKL

    with open('Hacene/modele de regresion lineaire.pkl', 'rb') as f:
        line_reg= pickle.load(f)

    with open('Hacene/modele de regression de Lasso.pkl', 'rb') as f:
        model_l = pickle.load(f)

    with open('Hacene/modele de regression de Ridge.pkl', 'rb') as f:
        model_r = pickle.load(f)

    with open('Hacene/modele de regression ElasticNet.pkl', 'rb') as f:
        model_en = pickle.load(f)

    with open('Hacene/best_lasso_model.pkl', 'rb') as f:
        model_best = pickle.load(f)


    if len(st.session_state.test_personne)>= 12:

        # affiche des predicitons par modele

        df_test = pd.DataFrame([st.session_state.test_personne], columns=st.session_state.nom_colonnes)
        df_test2 = pd.DataFrame([st.session_state.test_personne_2], columns=['age','sex','bmi','children','smoker','region'])
        st.write(f'model regression lineaire    {line_reg.predict(df_test)[0]:.2f}')
                
        st.write(f'model de Lasso               {model_l.predict(df_test)[0]:.2f}')

        st.write(f'model de Ridge               {model_r.predict(df_test)[0]:.2f}')
        
        st.write(f'model ElasticNet             {model_en.predict(df_test)[0]:.2f}')
        st.write(f'model best lasso             {model_best.predict(df_test2)[0]:.2f}')
        st.session_state.liste_pred = [line_reg.predict(df_test)[0],model_l.predict(df_test)[0],model_r.predict(df_test)[0],model_en.predict(df_test)[0], model_best.predict(df_test2)]
        st.session_state.liste_pred.sort(reverse=True)

        st.subheader(f'proposez un prix au client entre {float(st.session_state.liste_pred[0]):.2f} et {float(st.session_state.liste_pred[2]):.2f}')


        link_html = """
        <div style="text-align: center;">
            <a href="prediction_operateur" target="_self" style="font-size:20px; text-decoration: none; color: #0073e6;">REFAIRE LA SIMULATION</a>
        </div>
        """


        # if st.form_submit_button(' évaluez votre redevance') :
        if st.markdown(link_html, unsafe_allow_html=True):
            st.session_state.showform = False
            st.rerun()

