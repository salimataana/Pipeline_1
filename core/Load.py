from core.step import Step
from core.utils import DataSourceType

class Load(Step):

    def __init__(self, source_type: DataSourceType, output_path):
        self.kind = "load"
        self.data_source_type = source_type
        self.output_path = output_path

    def execute(self, data):
        data.to_csv(self.output_path, index=False)
        print(f"Données enregistrées dans : {self.output_path}")


