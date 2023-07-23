from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

Stage_01="Data Ingestion"

ingestion_obj=DataIngestion()
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stage_01_name} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stage_01_name=Stage_01))
data_df=ingestion_obj.initiate_data_ingestion()


Stage_02="Data Transformation"

transformation_obj=DataTransformation()
logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stage_02_name} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stage_02_name=Stage_02))
corpus,dataset=transformation_obj.initiate_data_transformation(dataset=data_df)


Satge_03="Model Trainer"

logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Stage {stage_03_name} initiated<<<<<<<<<<<<<<<<<<<<<<<<'.format(stage_03_name=Satge_03))
model_trainer_obj=ModelTrainer()
obj=model_trainer_obj.initiate_model_trainer(dataset=dataset,corpus=corpus)
