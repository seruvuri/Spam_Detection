
from dataclasses import dataclass
from src.utils import *
import pandas as pd
from colorama import Fore

@dataclass
class DataIngestion:
    @ensure_annotations
    def initiate_data_ingestion(self):
        try:
            config=read_yaml(path_to_yaml='config\config.yaml')
            logging.info('Reading Mongodb metadata from config file')

            collection,database_name,result=MongoDB_con(url=config['Mongo_database']['url'],database_name=config['Mongo_database']['Database'],collection_name=config['Mongo_database']['Collection'])
            

            # checking database is valid or not
            if ((config['Mongo_database']['Database'] not in database_name)):
                    #error message will be printed in red color if database name is not in mongodb 
                    print(Fore.RED + "Connection failed. Check Database is valid from the list {datasbase_name_list} in Config file ".format(datasbase_name_list=database_name))
                    exit()
            #checking whether collection is empty or not
            elif(len(result)==0):
                 #error will be peinted on screeen with yellow if data in collection is empty and will stop the execution of program
                 print(Fore.YELLOW + 'Database Collection is empty to proceed further')
                 exit()
            #if above conditions are fine then we convert the data into dataframe
            else:
                logging.info('Database Connection is valid')
                logging.info('Coverting Jsondata to Pandas Dataframe')
                json_df=collection.find()
                dataset=pd.json_normalize(json_df)
                dataset.to_csv(config['Artifacts_root']['raw_file'],header=True,index=False)
                logging.info('Saved data to file path "{file_path}"'.format(' ',file_path=config['Artifacts_root']['raw_file']))
            
            
                return dataset

        except Exception as e:
            raise CustomException(e,sys)