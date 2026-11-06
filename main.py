from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationPipeline


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()

    logger.info(f">>>>>>>>>> stage {STAGE_NAME} Competed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>> Stage : {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()

    logger.info(f">>>>>> Stage : {STAGE_NAME} ended <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e