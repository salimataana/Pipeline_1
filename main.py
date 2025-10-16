from core.extract import Extract
from core.transform import Transform
from core.Load import Load
from core.utils import DataSourceType
from pipeline import Pipeline


# Étapes du pipeline pour un seul fichier
extract = Extract(source_type=DataSourceType.FILE, path=r"C:\Users\Moi\Desktop\Contient_Bureau\Datasets\annual-enterprise-survey-2023-financial-year-provisional.csv")
transform = Transform()
load = Load(source_type=DataSourceType.FILE, output_path=r"C:\Users\Moi\Desktop\Contient_Bureau\Datasets\Result_Clean.csv")

# Création du pipeline
pipeline = Pipeline(steps=[extract, transform, load])

# Exécution du pipeline
pipeline.run()


# ---------------------------------------------
# 💡 Si tu veux extraire plusieurs fichiers, tu peux faire comme suit :
"""
inputs = ["data/toto.csv", "data/tata.csv"]
extracts = []

for input_path in inputs:
    extracts.append(Extract(source_type=DataSourceType.FILE, path=input_path))

transform = Transform(source_type=DataSourceType.FILE)

# Pour chaque extraction, on crée un pipeline avec les étapes transform et load
for extract in extracts:
    pipeline = Pipeline(steps=[extract, transform, load])
    pipeline.run()  # Pense à exécuter le pipeline ici pour chaque fichier
"""