import unittest
import pandas as pd
from core.transform import Transform
from core.utils import DataSourceType

class TestTransformStep(unittest.TestCase):

    def setUp(self):
        # Données de test
        self.input_data = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie"],
            "Year": [2023, 2025, 2024]
        })

        # Données attendues après transformation
        self.expected_data = pd.DataFrame({
            "Name": ["Alice", "Charlie"],
            "Year": [2023, 2024]
        }).reset_index(drop=True)

    def test_transform_filter_year(self):
        # Création de l'étape Transform
        transform_step = Transform(DataSourceType.FILE)

        # Exécution de la méthode execute()
        result = transform_step.execute(self.input_data).reset_index(drop=True)

        # Vérification que les données ont été filtrées correctement
        pd.testing.assert_frame_equal(result, self.expected_data)

if __name__ == "__main__":
    unittest.main()
