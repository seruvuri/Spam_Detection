from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

Stage_01="Data Ingestion"

ingestion_obj=DataIngestion()
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stage_01_name} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stage_01_name=Stage_01))
data_df=ingestion_obj.initiate_data_ingestion()


Stage_02="Data Transformation"

transformation_obj=DataTransformation()
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stage_02_name} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stage_02_name=Stage_02))
obj=transformation_obj.initiate_data_transformation(dataset=data_df)