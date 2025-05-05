# Projet Avion : Prédiction de la satisfaction des passagers

Ce projet utilise le dataset [Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction) pour prédire la satisfaction des passagers d'une compagnie aérienne en fonction de différentes variables liées aux caractéristiques des passagers et à leur expérience avec la compagnie aérienne.

## Prérequis

- Python 3.7+
- `pip` (pour installer les dépendances)
- Un environnement virtuel est recommandé

## Installation

1. **Clonez ce projet :**
```bash
git clone https://github.com/meliremi/projet.git

# Accédez au répertoire du projet :
bash
Copier
Modifier
cd projet_avion

# Créez un environnement virtuel :
bash
Copier
Modifier
python -m venv venv

#Activez l'environnement virtuel :
# Windows :
bash
Copier
Modifier
venv\Scripts\activate

# Mac/Linux :
bash
Copier
Modifier
source venv/bin/activate

# Installez les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Structure des fichiers



Utilisation
Activez l'environnement virtuel comme indiqué précédemment.

Exécutez l'application en lançant le script app.py :
bash
Copier
Modifier
python app.py

Ce script démarre le processus de prédiction de la satisfaction des passagers. Il utilise les données d'entrée et les passe à travers le modèle pour générer des prédictions.

Contribuer
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, n'hésitez pas à créer une pull request.

Pour contribuer :
Fork ce repository.

Créez une branche pour votre fonctionnalité (git checkout -b feature/ma-fonctionnalite).

Commitez vos changements (git commit -m 'Ajout de la fonctionnalité').

Poussez sur votre branche (git push origin feature/ma-fonctionnalite).

Ouvrez une pull request.

Licence
Ce projet est sous la licence MIT.

Notes supplémentaires
random_forest_model.pkl et label_encoders.pkl sont des fichiers volumineux et ont été supprimés de l'historique Git, ils peuvent être réajoutés si nécessaire à l'aide de Git Large File Storage (Git LFS). Si vous avez besoin de ces fichiers, vous pouvez les récupérer en réexécutant le code d'entraînement.

Le dataset original provient de Kaggle.
markdown
Copier
Modifier

---

## Structure des fichiers

Le projet est organisé de la manière suivante :

projet_avion/
├── app.py                         # Script principal pour démarrer l'application
├── requirements.txt              # Dépendances nécessaires au projet
├── .gitignore                    # Fichiers/répertoires à ignorer par Git
├── pyvenv.cfg                    # Configuration de l’environnement virtuel
├── source/
│   └── Scripts/
│       ├── data_cleaning.py      # Nettoyage des données brutes
│       ├── data_exploration.py   # Exploration des données + visualisations
│       ├── model.py              # Modèle de machine learning (random forest)
│       ├── random_forest_model.pkl # Modèle ML sauvegardé (supprimé du Git)
│       └── label_encoders.pkl    # Encodeurs des colonnes catégorielles
├── templates/
│   └── index.html                # Interface web HTML (si utilisée)
└── venv/                         # Environnement virtuel Python (à ignorer dans Git)

> **Note** : Les fichiers `.pkl` sont volumineux, donc supprimés du dépôt Git. Ils peuvent être régénérés en exécutant les scripts correspondants.



### Explication du contenu :

1. **Titre et Description** : Présente brièvement le projet et sa finalité.
2. **Prérequis et Installation** : Détaille les étapes pour installer l'environnement et le projet, en insistant sur l'usage d'un environnement virtuel.
3. **Structure des fichiers** : Donne une vue d'ensemble de l'organisation du projet, expliquant chaque répertoire et fichier.
4. **Utilisation** : Indique comment démarrer l'application et utiliser le projet.
5. **Contribuer** : Si tu souhaites que d'autres personnes contribuent au projet, cette section leur indique la marche à suivre.
6. **Licence** : Précise la licence sous laquelle le projet est distribué, ici la licence MIT par défaut.








