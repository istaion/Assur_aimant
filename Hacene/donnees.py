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


#création du dataframe

df = pd.read_csv('Hacene/dataset.csv')
df.drop_duplicates(inplace=True)

# Définir les tranches de BMI
bins = [0, 18.5, 24.9, 29.9, 40, 100]  # Tranches de BMI
labels = ['Sous-poids', 'Poids normal', 'Surpoids', 'Obésité', 'Obésité sévère']

# Ajouter une nouvelle colonne dans le DataFrame pour les tranches de BMI
df['BMI_category'] = pd.cut(df['bmi'], bins=bins, labels=labels, right=False)

#Label encoder pour le sexe et si les usagers sont fumeurs

labe_encod = LabelEncoder()
df['sex_encode']= labe_encod.fit_transform(df['sex'])
df['smoker_encode']= labe_encod.fit_transform(df['smoker'])

# encodage par région et par bmi category

df_reg_encod = pd.get_dummies(df['region'])
df_reg_encod.replace(False, 0, inplace=True)
df_reg_encod.replace(True, 1, inplace=True)


df_bmi_encod = pd.get_dummies(df['BMI_category'])
df_bmi_encod.replace(False, 0, inplace=True)
df_bmi_encod.replace(True, 1, inplace=True)

#concatener les df encodé avec le df

df_2 = pd.concat([df,df_reg_encod,df_bmi_encod], axis=1)
#supprimer les colonnes qui ont été encodés

df_2.drop(columns=['sex','smoker','region','BMI_category'],inplace=True)

#création du modèle linéaire

line_reg = LinearRegression()
X_train, X_test, y_train, y_test =train_test_split(df_2.drop('charges', axis = 1), df_2['charges'],random_state=42, test_size=0.2, stratify=df_2[['smoker_encode']])
line_reg.fit(X_train,y_train)

