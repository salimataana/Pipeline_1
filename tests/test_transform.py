import pandas as pd
import pytest
from core.transform import Transform
from core.utils import DataSourceType


def test_transform_execute():
    # Données de test
    data = pd.DataFrame({
        "Year": [2023, 2026, 2024, None],
        "Variable_name": ["Revenue", "Profit", "Loss", "Cost"],
        "Variable_category": ["Financial performance", "Other", "Financial performance", "Financial performance"],
        "Value": [100, 200, None, 400]
    })

    transform = Transform(source_type=DataSourceType.FILE)

    # Appliquer la transformation
    result = transform.execute(data)

    # Vérifier que les lignes avec valeurs manquantes ont été supprimées
    assert result.isnull().sum().sum() == 0

    # Vérifier qu’il n’y a pas d’année >= 2025
    assert (result["Year"] < 2025).all()

    # Vérifier que la colonne a bien été renommée
    assert "VarName" in result.columns
    assert "Variable_name" not in result.columns

    # Vérifier qu’il ne reste que les lignes avec "Financial performance"
    assert result["Variable_category"].eq("Financial performance").all()
