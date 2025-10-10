🧩 Projet ETL Modulaire en Python
Ce projet est une implémentation d’un pipeline ETL (Extraction, Transformation, Chargement) modulaire. Il permet de traiter des données en plusieurs étapes indépendantes et testées.

🎯 Objectif
Extraire les données (depuis un fichier CSV ou base de données)

Transformer les données (nettoyage ou traitement)

Charger les données transformées dans un fichier final

📁 Structure du projet


.
├── core/
│   ├── step.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
├── pipeline.py
├── main.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   ├── test_pipeline.py
│   └── test_steps.py
└── README.md

🧪 Tests
Chaque étape du pipeline est testée avec unittest pour garantir la fiabilité des résultats.

🚀 Lancement
Exécution du pipeline à partir du fichier main.py. Il orchestre l’enchaînement des étapes.

📌 À propos
Ce projet a été développé pour apprendre à structurer proprement un pipeline de traitement de données en Python, tout en appliquant de bonnes pratiques de modularité et de test.


AnaSalimata-Sanou-ex1