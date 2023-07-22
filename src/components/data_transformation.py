from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from ensure import ensure_annotations
import sys
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

@dataclass
class DataTransformation:

    def initiate_data_transformation(self,dataset:pd.DataFrame):
        try:
            logging.info('checking if data is available in dataframe')
            if len(dataset)==0:
                print(' dataframe is empty to proceed further. please check Dataset')
            else:
                print('data is available in dataframe')
        except Exception as e :
            raise CustomException(e,sys)