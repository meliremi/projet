from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Chemins des fichiers modèle et encodeurs
MODEL_PATH = "C:/Users/remila/Desktop/projet python/projet_avion/source/scripts/random_forest_model.pkl"
ENCODERS_PATH = "C:/Users/remila/Desktop/projet python/projet_avion/source/scripts/label_encoders.pkl"

# Chargement du modèle et des encodeurs
try:
    model = joblib.load(MODEL_PATH)
    encoders = joblib.load(ENCODERS_PATH)
    print("✅ Modèle et encodeurs chargés avec succès")
except Exception as e:
    print(f"❌ Erreur de chargement : {str(e)}")
    raise

# Colonnes d'entrée
FEATURE_COLUMNS = [
    'Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',
    'Flight Distance', 'Inflight wifi service', 'Departure/Arrival time convenient',
    'Ease of Online booking', 'Gate location', 'Food and drink', 'Online boarding',
    'Seat comfort', 'Inflight entertainment', 'On-board service', 'Leg room service',
    'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness',
    'Departure Delay in Minutes', 'Arrival Delay in Minutes'
]

NUMERIC_COLS = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form.to_dict()
        print("📥 Données reçues:", form_data)

        # Construction du DataFrame
        data = {}
        for col in FEATURE_COLUMNS:
            val = form_data.get(col, '')
            if col in NUMERIC_COLS:
                try:
                    data[col] = [float(val)]
                except ValueError:
                    data[col] = [0.0]
            else:
                data[col] = [val if val != '' else "Unknown"]

        df = pd.DataFrame(data)
        print("\n🔍 Données AVANT encodage :")
        print(df)

        # Encodage avec fallback intelligent
        for col, encoder in encoders.items():
            if col in df.columns:
                original_val = df[col].values[0]
                try:
                    df[col] = encoder.transform(df[col])
                except ValueError:
                    print(f"⚠️ Valeur inconnue pour {col} : '{original_val}'")
                    fallback_val = encoder.classes_[0]
                    df[col] = encoder.transform([fallback_val])
                    print(f"➡️ Remplacé par valeur par défaut : '{fallback_val}'")

        print("\n✅ Données APRÈS encodage :")
        print(df)

        # Prédiction
        prediction = model.predict(df)[0]
        result = "satisfied" if prediction == 1 else "neutral or dissatisfied"

        print(f"\n🔮 Prédiction : {result}")

        return jsonify({
            'success': True,
            'prediction': result,
            'message': f"Prédiction : {result}"
        })

    except Exception as e:
        print(f"❌ Erreur de prédiction : {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
