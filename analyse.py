import pandas as pd
import os

# Chemin relatif vers les fichiers CSV dans venv/data
train_path = os.path.join("venv", "data", "train.csv")
test_path = os.path.join("venv", "data", "test.csv")

# Charger les fichiers CSV
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Afficher les premières lignes des datasets pour vérifier
print("📊 Train Dataset :")
print(train_df.head())

print("\n📊 Test Dataset :")
print(test_df.head())

# Vérifier la répartition de la satisfaction dans le dataset train
print("\n📊 Répartition de la satisfaction dans le dataset train :")
print(train_df['satisfaction'].value_counts())  # Comptabiliser les valeurs uniques dans 'satisfaction'
# Supprimer la colonne "Unnamed: 0" qui est inutile
train_df = train_df.drop(columns=["Unnamed: 0"])
test_df = test_df.drop(columns=["Unnamed: 0"])

# Afficher les premières lignes après suppression pour vérifier
print("\n📊 Train Dataset après nettoyage :")
print(train_df.head())

print("\n📊 Test Dataset après nettoyage :")
print(test_df.head())
# Vérifier les valeurs manquantes dans les datasets
print("\n📊 Valeurs manquantes dans le Train Dataset :")
print(train_df.isnull().sum())

print("\n📊 Valeurs manquantes dans le Test Dataset :")
print(test_df.isnull().sum())
