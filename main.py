from src.logger import logging
from src.components.data_ingestion import DataIngestion
#from src.components.data_transformation import DataTransformation

IngestionStage_01="Data Ingestion"

ingestion_obj=DataIngestion()
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stagename} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stagename=IngestionStage_01))
data_df=ingestion_obj.initiate_data_ingestion()