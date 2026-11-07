from mlproject import logger
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer



STAGE_NAME = "Model Trainer"


class ModelTrainerPipeline:
    def __int__(self):
        pass


    def main(self):
        config = ConfigurationManager()

        model_trainer_config = config.get_model_trainer_config()

        model_trainer = ModelTrainer(config=model_trainer_config)

        model_trainer.train()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage : {STAGE_NAME} Started <<<<<<<<< ")
        obj = ModelTrainerPipeline()
        obj.main()

        logger.info(f">>>>>>>>> stage : {STAGE_NAME} Ended <<<<<<<<< ")
    except Exception as e:
        logger.exception(e)
        raise e