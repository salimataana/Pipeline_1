import unittest
import pandas as pd
import os
from core.extract import Extract
from core.utils import DataSourceType

class TestExtractStep(unittest.TestCase):

    def setUp(self):
        """Méthode exécutée avant chaque test"""
        # Création d’un DataFrame simple pour le test
        self.test_data = pd.DataFrame({
            "col1": [1, 2],
            "col2": ["a", "b"]
        })

        # Définition du chemin du fichier temporaire
        self.test_csv_path = "test_file.csv"

        # Sauvegarde du DataFrame dans un fichier CSV
        self.test_data.to_csv(self.test_csv_path, index=False)

    def tearDown(self):
        """Méthode exécutée après chaque test pour nettoyer"""
        # Suppression du fichier temporaire après le test
        if os.path.exists(self.test_csv_path):
            os.remove(self.test_csv_path)

    def test_extract_file(self):
        """Test que la classe Extract lit correctement un fichier CSV"""
        # Création de l'étape Extract
        extract_step = Extract(DataSourceType.FILE, self.test_csv_path)

        # Exécution de la méthode execute()
        result = extract_step.execute()

        # Vérification que le résultat est identique au DataFrame original
        pd.testing.assert_frame_equal(result, self.test_data)

if __name__ == "__main__":
    unittest.main()
