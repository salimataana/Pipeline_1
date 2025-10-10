from pyspark.sql import SparkSession
from cores.step import Step
from cores.utils import DataSourceType
import os

class Extract(Step):

    def __init__(self, source_type: DataSourceType, path, spark: SparkSession):
        self.kind = "extract"
        self.data_source_type = source_type
        self.path = path
        self.spark = spark  # SparkSession injectée

    def execute(self, data=None):
        if self.data_source_type == DataSourceType.FILE:
            # Dictionnaire extension → format Spark
            format_map = {
                ".csv": "csv",
                ".json": "json",
                ".parquet": "parquet",
                ".orc": "orc",
                ".avro": "avro",  # nécessite spark-avro
                ".xml": "xml"      # nécessite spark-xml
            }

            # Récupérer l'extension
            ext = os.path.splitext(self.path)[1].lower()
            fmt = format_map.get(ext)

            if fmt is None:
                raise ValueError(f"Format non supporté : {ext}")

            # Lire le fichier selon le format
            if fmt == "csv":
                df = self.spark.read.format(fmt).option("header", True).option("inferSchema", True).load(self.path)
            elif fmt == "xml":
                df = self.spark.read.format(fmt).option("rowTag", "row").load(self.path)
            else:
                # JSON, Parquet, ORC, Avro : options par défaut
                df = self.spark.read.format(fmt).load(self.path)

        return df
