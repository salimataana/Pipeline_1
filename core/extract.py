import pandas as pd
from core.step import Step
from core.utils import DataSourceType

class Extract(Step):

    def __init__(self, source_type: DataSourceType, path):
        self.kind = "extract"
        self.data_source_type = source_type
        self.path = path

    def execute(self, data = None):
        # if source_type == db:
        # extract with uri : jdbc
        # if source_type == file:
        if self.data_source_type == DataSourceType.FILE:
            data = pd.read_csv(self.path)
        return data


        # extact file
        # if file_type == csv
        # format(csv)
        # if


