import os
import pandas as pd
from mlproject import logger
from mlproject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)->bool:

        try :
            validation_satus = None

            data = pd.read_csv(self.config.unzip_data_dir , sep=";")
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()



            for col in all_cols:
                if col not in all_schema:
                    validation_satus = False
                else:
                    validation_satus = True

                with open(self.config.STATUS_FILE , "w") as f:
                    f.write(f'Validation Status : {validation_satus}')


            return validation_satus


    
        except Exception as e:
            logger.exception(e)
            raise e