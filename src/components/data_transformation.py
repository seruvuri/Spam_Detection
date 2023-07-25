
from dataclasses import dataclass
import sys
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from src.utils import *
@dataclass
class DataTransformation:

    @ensure_annotations
    def initiate_data_transformation(self,dataset:pd.DataFrame):
        try:
            config=read_yaml(path_to_yaml='config\config.yaml')
            logging.info('checking if data is available in dataframe')
            if len(dataset)==0:
                print(' dataframe is empty to proceed further. please check Dataset')
                exit()
            else:
                global corpus
                dataset=dataset.drop(config['Dataframe']['extra_column'],axis=1)
                #print(dataset.info())
                corpus=[]
                logging.info("creating object for lemmatization")
                wordnet=WordNetLemmatizer()
                for i in range(0,len(dataset)):
                    #'removing "[.,?/\@#$%^*()+!]" from input column using regular expression
                    review=re.sub('[^a-zA-Z]',' ',dataset[config['Dataframe']['input_column']][i])
                    #converting all Upper characters from upper case to lower case
                    review=review.lower()
                    review=review.split()
                    #applying lemmatization on the input column
                    review=[wordnet.lemmatize(word)for word in review if word not in stopwords.words('english')]
                    review=' '.join(review)
                    #appending final text to corpus list
                    corpus.append(review)
            #print(corpus)
            return corpus,dataset
                    
        except Exception as e :
            raise CustomException(e,sys)