from core.step import Step
from core.utils import DataSourceType


class Transform(Step):

    def __init__(self):
        self.kind = "transform"

    def execute(self, data):
        # Nettoyer les valeurs manquantes
        data = data.dropna()

        # Filtrer les années
        data = data[data["Year"] < 2025]

        # Renommer une colonne
        data = data.rename(columns={"Variable_name": "VarName"})

        # Filtrer les lignes où la Variable_category est "Financial performance"
        data = data[data["Variable_category"] == "Financial performance"]

        return data



# Les différentes transformations
        #  transformer les données :
        #  Nettoyer les valeurs manquantes
        #  Renommer des colonnes
        #  Créer de nouvelles colonnes
        #  Filtrer les lignes
