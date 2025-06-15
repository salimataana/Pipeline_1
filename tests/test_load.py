import unittest
import pandas as pd
import os
from core.Load import Load
from core.utils import DataSourceType

class TestLoadStep(unittest.TestCase):

    def setUp(self):
        """Prépare un DataFrame et un chemin de fichier de sortie"""
        self.test_data = pd.DataFrame({
            "Nom": ["Alice", "Bob"],
            "Age": [25, 30]
        })
        self.output_path = "output_test.csv"

    def tearDown(self):
        """Supprime le fichier après le test"""
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_load_to_csv(self):
        """Vérifie que les données sont bien enregistrées dans un fichier CSV"""
        load_step = Load(DataSourceType.FILE, self.output_path)
        load_step.execute(self.test_data)

        # Lire le fichier et comparer les données
        loaded_data = pd.read_csv(self.output_path)
        pd.testing.assert_frame_equal(loaded_data, self.test_data)

if __name__ == "__main__":
    unittest.main()
