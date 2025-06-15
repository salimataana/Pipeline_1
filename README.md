🧩 Projet ETL Modulaire en Python
Ce projet est une implémentation d’un pipeline ETL (Extraction, Transformation, Chargement) modulaire. Il permet de traiter des données en plusieurs étapes indépendantes et testées.

🎯 Objectif
Extraire les données (depuis un fichier CSV ou base de données)

Transformer les données (nettoyage ou traitement)

Charger les données transformées dans un fichier final

📁 Structure du projet







.
├── core/
│   ├── step.py               # Classe abstraite Step
│   ├── extract.py            # Étape d'extraction
│   ├── transform.py          # Étape de transformation
│   ├── load.py               # Étape de chargement
│   └── utils.py              # Fonctions utilitaires (ex: DataSourceType)
│
├── pipeline.py               # Déroulement du pipeline complet
├── main.py                   # Point d'entrée pour exécuter le pipeline
│
├── tests/
│   ├── test_extract.py       # Test pour l'extraction
│   ├── test_transform.py     # Test pour la transformation
│   ├── test_load.py          # Test pour le chargement
│   ├── test_pipeline.py      # Test pour tout le pipeline
│   └── test_steps.py         # Test pour la classe Step (comportement abstrait ou héritage)
│
└── README.md                 # Description du projet








🧪 Tests
Chaque étape du pipeline est testée avec unittest pour garantir la fiabilité des résultats.

🚀 Lancement
Exécution du pipeline à partir du fichier main.py. Il orchestre l’enchaînement des étapes.

📌 À propos
Ce projet a été développé pour apprendre à structurer proprement un pipeline de traitement de données en Python, tout en appliquant de bonnes pratiques de modularité et de test.