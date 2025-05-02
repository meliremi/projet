import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les fichiers CSV nettoyés
train_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/train_cleaned.csv"
test_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/test_cleaned.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Visualisation de la répartition de la satisfaction
plt.figure(figsize=(12, 6))
sns.countplot(x='satisfaction', data=train_df)
plt.title('Répartition de la Satisfaction - Train Dataset')
plt.show()

# Vérification de la corrélation entre les variables numériques
numeric_cols = train_df.select_dtypes(include=['float64', 'int64']).columns
corr = train_df[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black', fmt='.2f')
plt.title('Matrice de Corrélation des Variables Numériques')
plt.show()

# Distributions des variables numériques
plt.figure(figsize=(15, 10))
plt.subplot(2, 4, 1)
sns.histplot(train_df['Age'], kde=True, bins=30)
plt.title('Distribution de l\'Age - Train Dataset')
plt.subplot(2, 4, 2)
sns.histplot(train_df['Flight Distance'], kde=True, bins=30)
plt.title('Distribution de la Distance de Vol - Train Dataset')
plt.subplot(2, 4, 3)
sns.histplot(train_df['Arrival Delay in Minutes'], kde=True, bins=30)
plt.title('Distribution du Délai d\'Arrivée - Train Dataset')
plt.subplot(2, 4, 4)
sns.histplot(train_df['Departure Delay in Minutes'], kde=True, bins=30)
plt.title('Distribution du Délai de Départ - Train Dataset')
plt.tight_layout()
plt.show()

# Visualisation des relations entre variables catégorielles
plt.figure(figsize=(12, 6))
sns.countplot(x='Gender', data=train_df)
plt.title('Répartition des Genres - Train Dataset')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Customer Type', data=train_df)
plt.title('Répartition du Type de Client - Train Dataset')
plt.show()
