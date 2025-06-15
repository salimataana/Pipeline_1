import unittest
from pipeline import Pipeline
from core.step import Step

# Étapes fictives pour le test
class MockExtract(Step):
    def execute(self, data=None):
        return [1, 2, 3]

class MockTransform(Step):
    def execute(self, data):
        return [x * 2 for x in data]

class MockLoad(Step):
    def execute(self, data):
        self.saved_data = data
        return data

class TestPipeline(unittest.TestCase):

    def test_pipeline_run(self):
        # Création des étapes
        extract = MockExtract()
        transform = MockTransform()
        load = MockLoad()

        # Création du pipeline avec les étapes
        pipeline = Pipeline(steps=[extract, transform, load])

        # Exécution du pipeline
        result = pipeline.run()

        # Vérifications
        self.assertEqual(result, [2, 4, 6])
        self.assertEqual(load.saved_data, [2, 4, 6])  # Vérifie que les données sont bien "chargées"

if __name__ == '__main__':
    unittest.main()
