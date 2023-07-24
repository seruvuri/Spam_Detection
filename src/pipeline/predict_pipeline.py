import sys,os
import pandas as pd
from src.utils import *

from dataclasses import dataclass

@dataclass
class Predictpipeline:
    
    def predict(self,features):
        try:
           config=read_yaml(path_to_yaml='config\config.yaml')
           model_path=config['Artifacts_root']['model_obj']
           model=load_object(config['Artifacts_root']['model_obj'])
           preprocessor=load_object(file_path=config['Artifacts_root']['preprocessor_obj'])
           data_scaled=preprocessor.transform(features).toarray()
           preds=model.predict(data_scaled)
           return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    
    def __init__(self,message:str):
        self.message=message

    def get_data_as_frame(self):
        try:
            custom_data_input_dict={
                "message":[self.message]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
           