import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
import joblib

# 1. Charger les datasets
train_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/train_cleaned.csv"
test_path = "C:/Users/remila/Desktop/projet python/projet_avion/venv/data/test_cleaned.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)


# 2. Supprimer la colonne 'id' si elle existe
if 'id' in train_df.columns:
    train_df.drop(columns=['id'], inplace=True)
if 'id' in test_df.columns:
    test_df.drop(columns=['id'], inplace=True)

# 3. Encodage des colonnes catégorielles
encoders = {}
categorical_cols = train_df.select_dtypes(include='object').columns.drop('satisfaction')

for col in categorical_cols:
    le = LabelEncoder()
    train_df[col] = le.fit_transform(train_df[col])
    test_df[col] = le.transform(test_df[col])  # Attention à utiliser les mêmes classes
    encoders[col] = le

# Encodage de la target
target_encoder = LabelEncoder()
train_df['satisfaction'] = target_encoder.fit_transform(train_df['satisfaction'])
test_df['satisfaction'] = target_encoder.transform(test_df['satisfaction'])
encoders['satisfaction'] = target_encoder

# 4. Séparer features et labels
X_train = train_df.drop(columns=['satisfaction'])
y_train = train_df['satisfaction']
X_test = test_df.drop(columns=['satisfaction'])
y_test = test_df['satisfaction']

# 5. Équilibrage des classes avec SMOTE
sm = SMOTE(random_state=42)
X_resampled, y_resampled = sm.fit_resample(X_train, y_train)

# 6. Entraînement du modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_resampled, y_resampled)

# 7. Évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 8. Sauvegarde du modèle et des encodeurs
joblib.dump(model, "random_forest_model.pkl")
joblib.dump(encoders, "label_encoders.pkl")
print(" Modèle et encodeurs sauvegardés avec succès.")
