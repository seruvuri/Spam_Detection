import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="Spam_Detection"

list_of_files=[
    f"notebook/{project_name}.ipynb",
    f"artifacts/raw.csv",
    "requirements.txt",
    "README.md",
    "setup.py",
    "main.py",
    f"config/config.yaml",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/predict_pipeline.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/logger.py",
    f"src/exception.py",
    f"templates/home.html",
    f"templates/index.html",
    "application.py",
    f"src/utils.py"
]


for filepath in list_of_files:
    #handeling forward slash path
    filepath=Path(filepath)
    #for seperate folder name and file name
    filedir,filename=os.path.split(filepath)# will return ex:'config'  'config.yaml'


    if filedir !="":
        #creating directory
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for file:{filename}")

        #checking file is present and size of file is available then we wont replace existing file
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        #no file present will create file
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exists")