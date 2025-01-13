import streamlit as st
from donnees import df_2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
        imc = int_poids / ((int_taille /100) ** 2)

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

    nb_enfant = int(st.radio("combien d'enfants",[0,1,2,3,4,5]))
    sexe = st.radio('êtes-vous un homme ou une femme', ('Homme','Femme'))
    fumeur = st.radio('Fumez-vous?',('oui','non'))
    region = st.selectbox('de quel region venez vous ?', ['northeast', 'northwest', 'southeast','southwest'])

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



    test_personne = [age,nb_enfant,cat_sexe,cat_fumeur]
    for element in cat_region:
        test_personne.append(element)
    for element in imc_cat:
        test_personne.append(element)

    nom_colonnes = df_2.drop(['charges', 'bmi'],axis = 1).columns



    if st.form_submit_button(' évaluez votre redevance') :
        pass


# st.write(df_test)

line_reg = LinearRegression()
X_train, X_test, y_train, y_test =train_test_split(df_2.drop(['charges', 'bmi'], axis = 1), df_2['charges'],random_state=42, test_size=0.2, stratify=df_2[['smoker_encode']])
line_reg.fit(X_train,y_train)

model = make_pipeline(StandardScaler(), PolynomialFeatures(2), Ridge(alpha=12.66, random_state=42))

X_train, X_test, y_train, y_test =train_test_split(df_2.drop(['charges', 'bmi'], axis = 1), df_2['charges'],random_state=42, test_size=0.15, stratify=df_2[['smoker_encode']])
model.fit(X_train,y_train)

model_l = make_pipeline(StandardScaler(),
                       PolynomialFeatures(interaction_only=True), Lasso(alpha=70, random_state=42))

X_train, X_test, y_train, y_test =train_test_split(df_2.drop(['charges', 'bmi'], axis = 1), df_2['charges'],random_state=42, test_size=0.15, stratify=df_2[['smoker_encode']])
model_l.fit(X_train,y_train)

model_en = make_pipeline(StandardScaler(), PolynomialFeatures(interaction_only= True), ElasticNet(alpha=70, l1_ratio=1, random_state=42))

X_train, X_test, y_train, y_test =train_test_split(df_2.drop(['charges','bmi'], axis = 1), df_2['charges'],random_state=42, test_size=0.15, stratify=df_2[['smoker_encode']])
model_en.fit(X_train,y_train)




if len(test_personne)>= 12:
    df_test = pd.DataFrame([test_personne], columns=nom_colonnes)
    st.subheader(f'model regression lineaire{line_reg.predict(df_test)}')
            
    st.subheader(f'model de Lasso {model_l.predict(df_test)}')

    st.subheader(f'model de Ridge {model.predict(df_test)}')
    
    st.subheader(f'model ElasticNet {model_en.predict(df_test)}')



    link_html = """
    <div style="text-align: center;">
        <a href="prediction" target="_self" style="font-size:20px; text-decoration: none; color: #0073e6;">REFAIRE LA SIMULATION</a>
    </div>
    """


    st.markdown(link_html, unsafe_allow_html=True)

    
# if clique:
#     st.write(f'model regression lineaire{line_reg.predict(df_test)}')
#     st.write(f'model de Lasso {model_l.predict(df_test)}')
#     st.write(f'model de Ridge {model.predict(df_test)}')


