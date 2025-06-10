from core.extract import Extract
from core.transform import Transform
from core.Load import Load
from core.utils import DataSourceType
from pipeline import Pipeline


# Étapes du pipeline
extract = Extract(source_type=DataSourceType.FILE, path=r"C:\Users\Moi\Desktop\Contient_Bureau\Datasets\annual-enterprise-survey-2023-financial-year-provisional.csv")
transform = Transform(source_type=DataSourceType.FILE)
load = Load(source_type=DataSourceType.FILE,output_path=r"C:\Users\Moi\Desktop\Contient_Bureau\Datasets\Result_Clean.csv")

# Création du pipeline
pipeline = Pipeline(steps=[extract, transform, load])

# Exécution du pipeline
pipeline.run()
