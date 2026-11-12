from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvluation
from mlproject import logger


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPiepline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        model_evaluation = ModelEvluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()



if __name__ == "__main__":

    try:
        logger.info(f">>>>>>>>>>> Stage : {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = ModelEvaluationPiepline()
        obj.main()
        logger.info(f">>>>>>>>>>> Stage : {STAGE_NAME} ended  <<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    