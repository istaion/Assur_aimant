
# Prédiction de Prime d'Assurance - Assur'Aimant

## Contexte

**Assur’Aimant**, un assureur français en pleine expansion sur le marché américain, souhaite automatiser l’estimation des primes d’assurance de ses souscripteurs pour accélérer et rendre plus précises ses évaluations. Actuellement, cette estimation repose sur des ratios manuels et l’expérience des courtiers, ce qui est à la fois long et coûteux.

Dans le cadre de cet appel d’offres, nous avons été sollicités pour concevoir une solution de prédiction des primes d’assurance en utilisant des techniques avancées d’intelligence artificielle et d’analyse de données. Ce projet vise à créer un modèle prédictif capable de calculer la prime d’assurance pour chaque souscripteur en fonction de différentes variables.

## Objectifs

L'objectif principal de ce projet est de prédire la prime d'assurance d'un souscripteur basé sur un ensemble de caractéristiques spécifiques. Le modèle doit être capable de :

- Estimer une prime d'assurance en fonction des données historiques.
- Automatiser le processus d'évaluation, le rendant plus rapide et plus précis.
- Réduire le recours à l'expérience manuelle des courtiers et des ratios traditionnels.
- Réaliser un POC avec streamlit

## Structure du projet

### 1. Collecte des Données

Les données collectées auprès d'**Assur’Aimant** incluent diverses informations sur les souscripteurs et leurs contrats. Nous avons extrait ces données pour construire un jeu de données exploitable pour notre modélisation.

#### Variables clés :
- **Informations sur le souscripteur** :
  - Âge
  - Sexe
  - Localisation géographique 
  - âge
  - IMC
  - nombre d'enfants
  - Montant de la franchise


### 2. Traitement des Données

Avant de pouvoir entraîner nos modèles d’IA, nous avons dû effectuer plusieurs étapes de prétraitement des données :

- Nettoyage des données : Gestion des valeurs manquantes, des erreurs de saisie et des incohérences.
- Normalisation des variables numériques pour faciliter l'entraînement des modèles.
- Encodage des variables catégorielles (ex. : sexe, catégorie IMC, etc.).
- Création de nouvelles variables dérivées des données existantes (par exemple, âge du véhicule).

### 3. Modélisation et Prédiction

Nous avons testé plusieurs modèles de machine learning pour la prédiction de la prime d’assurance :

- **Régression linéaire** : Pour un premier aperçu rapide des relations entre les variables.
- **Régression Lasso** : Pour un modèle linéaire plus robuste.
- **forêts aléatoires** : Pour capturer des interactions non linéaires et complexes.

Les modèles ont été évalués à l’aide de métriques telles que l'erreur absolue moyenne (MAE), la racine de l’erreur quadratique moyenne (RMSE), et le coefficient de détermination (R²).

### 4. Évaluation et Déploiement

Le modèle retenu sera déployé dans un environnement de production afin d’estimer les primes en temps réel, permettant à **Assur’Aimant** de remplacer les méthodes manuelles. Le modèle sera régulièrement mis à jour en fonction des nouvelles données recueillies pour assurer une performance optimale.

## Étapes à venir

- Affiner les modèles de prédiction avec de nouvelles données.
- Déployer le modèle dans l'environnement de production d’Assur’Aimant.
- Surveiller les performances du modèle et le réentraîner avec des données mises à jour.

## Technologies utilisées

- **Langages** : Python
- **Bibliothèques** :
  - Pandas, Numpy (pour le traitement des données)
  - Scikit-learn (modélisation et évaluation)

- **Outils** : Jupyter Notebook, Git, Docker (pour la containerisation et le déploiement)

## Installation

### Prérequis

- Python 3
- Pip (ou conda)

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancer le notebook

Pour explorer le code et les résultats dans un notebook Jupyter :

```bash
jupyter notebook
```

## Résultats attendus

En utilisant cette solution d'IA, nous prévoyons les résultats suivants pour **Assur’Aimant** :

- Réduction du temps nécessaire pour estimer une prime d’assurance.
- Amélioration de la précision des primes estimées, avec une réduction significative des erreurs humaines.
- Automatisation du processus, permettant une gestion plus efficace des souscripteurs.


## Auteurs

- [ZERROUK Hacène] 
- [POUTOT Victor]

