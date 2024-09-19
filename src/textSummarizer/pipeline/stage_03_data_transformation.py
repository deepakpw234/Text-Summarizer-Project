from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransforamtion
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransforamtion(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e