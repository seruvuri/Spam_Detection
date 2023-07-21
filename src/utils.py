from src.exception import CustomException
from src.logger import logging
import pymongo
import certifi
from box import ConfigBox
import sys
import yaml
from ensure import ensure_annotations
from pathlib import Path

#reading config.yaml file
@ensure_annotations
def read_yaml(path_to_yaml:str):
   try:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logging.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
   except Exception as e:
      raise CustomException(e,sys)
   
# mongoDB connection
@ensure_annotations
def MongoDB_con(url:str,database_name:str,collection_name:str):
    try:
        myclient=pymongo.MongoClient(url,tlsCAFile=certifi.where())
        global collection
        logging.info("mongoDB connection initiated")
        db=myclient[database_name]
        collection=db[collection_name]
        database_name=myclient.list_database_names()
        result=collection.find()
        result=list(result)
        return collection,database_name,result
    except Exception as e:
        raise CustomException(e,sys)