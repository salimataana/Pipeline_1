
from core.step import Step
from core.utils import DataSourceType


class Transform(Step):

    def __init__(self, source_type: DataSourceType):
        self.kind = "transform"
        self.data_source_type = source_type


    def execute(self, data):
        pass
        #  transformer les données :
        #  Nettoyer les valeurs manquantes
        #  Renommer des colonnes
        #  Créer de nouvelles colonnes
        #  Filtrer les lignes
        # Filtrer :
        data = data[data["Year"] > 2025]
        return data


