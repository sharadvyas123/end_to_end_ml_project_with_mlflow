from pathlib import Path
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTrnasformation
from mlproject import logger


STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt") , "r") as f:
                status = f.read().split(" ")[-1]



            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformaion_config()
                data_transformation = DataTrnasformation(config=data_transformation_config)


                data_transformation.train_test_splitting()

            else:
                raise Exception("Your Data Schema is not valid")
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage : {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()

        logger.info(f">>>>>>>> Stage : {STAGE_NAME} Ended <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e