import unittest
from core.step import Step

# Classe enfant pour tester Step
class DummyStep(Step):
    def execute(self, data):
        return data

class TestStep(unittest.TestCase):

    def test_execute_returns_input(self):
        step = DummyStep()
        data = {"key": "value"}
        result = step.execute(data)
        self.assertEqual(result, data)

if __name__ == "__main__":
    unittest.main()
