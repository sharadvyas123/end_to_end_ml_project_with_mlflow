import os
import joblib
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error , mean_absolute_error , r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from mlproject.entity.config_entity import ModelEvaluationConfig
from mlproject.utils.common import save_json

class ModelEvluation:
    def __init__(self ,config : ModelEvaluationConfig):
        self.config = config


    def eval_metrics(self , actual , pred):
        rmse = np.sqrt(mean_squared_error(actual , pred))
        mae = mean_absolute_error(actual , pred)

        r2 = r2_score(actual ,pred)
        return rmse , mae , r2


    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)


        test_x = test_data.drop([self.config.target_column] , axis= 1)
        test_y = test_data[[self.config.target_column]]


        # Runs and the Model Registry must use the same remote DagsHub store;
        # otherwise the registry cannot find the run when creating a version.
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)

        tracking_uri_type_store = urlparse(mlflow.get_registry_uri()).scheme


        with mlflow.start_run():
            predict_qualities = model.predict(test_x)

            (rmse , mae , r2) = self.eval_metrics(test_y , predict_qualities)


            scores = {"rmse" : rmse , "mae" : mae , "r2" : r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('rmse' , rmse)
            mlflow.log_metric('mae' , mae)
            mlflow.log_metric('r2' , r2)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model , "model" ,registered_model_name= "ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model , "model")
