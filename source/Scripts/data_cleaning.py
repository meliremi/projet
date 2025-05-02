import pandas as pd

# Charger les fichiers CSV
train_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/train.csv"
test_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/test.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Affichage des premières lignes des datasets
print(" Train Dataset :")
print(train_df.head())

print("\n Test Dataset :")
print(test_df.head())

# Supprimer la colonne "Unnamed: 0" qui est inutile
train_df = train_df.drop(columns=["Unnamed: 0"])
test_df = test_df.drop(columns=["Unnamed: 0"])

# Vérification des valeurs manquantes
print("\n Valeurs manquantes dans le Train Dataset :")
print(train_df.isnull().sum())

print("\n Valeurs manquantes dans le Test Dataset :")
print(test_df.isnull().sum())

# Remplacer les valeurs manquantes par la moyenne
train_df['Arrival Delay in Minutes'].fillna(train_df['Arrival Delay in Minutes'].mean(), inplace=True)
test_df['Arrival Delay in Minutes'].fillna(test_df['Arrival Delay in Minutes'].mean(), inplace=True)

# Vérification des valeurs manquantes après remplissage
print("\n Valeurs manquantes dans le Train Dataset après remplissage :")
print(train_df.isnull().sum())

print("\n Valeurs manquantes dans le Test Dataset après remplissage :")
print(test_df.isnull().sum())

# Sauvegarder les fichiers nettoyés
train_df.to_csv("C:/Users/remila/Desktop/projet python/projet_avion/venv/data/train_cleaned.csv", index=False)
test_df.to_csv("C:/Users/remila/Desktop/projet python/projet_avion/venv/data/test_cleaned.csv", index=False)

print("\n Fichiers nettoyés sauvegardés !")
