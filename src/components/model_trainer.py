from src.utils import *
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report,roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (RandomForestClassifier,
                              GradientBoostingClassifier)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC


@dataclass
class ModelTrainer:

    @ensure_annotations
    def initiate_model_trainer(self,dataset:pd.DataFrame,corpus:list):
        try:
            config=read_yaml(path_to_yaml='config\config.yaml')

            if len(dataset)!=len(corpus):
                print('corpus and dataframe data is not matching ')
            else:
                logging.info('creating object for tfidf')
                tfidf=TfidfVectorizer(max_features=config['TFIDF_parameters']['max_features'])
                logging.info('Transforming input feature with tfidf vectorizer')
                X=tfidf.fit_transform(corpus).toarray()
                logging.info('preparing target feature')
                y=pd.get_dummies(dataset[config['Dataframe']['target_column']])
                logging.info('choosing only one column after performing get dummies')
                y=y.iloc[:,1].values


                logging.info('Splitting data into train and test')
                X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=config['Model_Training_Parameters']['test_size'],random_state=config['Model_Training_Parameters']['random_state'])
                logging.info('data is splitted into "X_train:{X_train_size}","X_test{X_test_size}","y_train:{y_train_size}","y_test:{y_test_size}"'.format(X_train_size=
                                                                                                                                                   X_train.shape,
                                                                                                                                                   X_test_size=X_test.shape,
                                                                                                                                                   y_train_size=y_train.shape,
                                                                                                                                                   y_test_size=y_test.shape))
                
                Models={
                    "Logistic Regression":LogisticRegression(),
                    "Knearest neighbor":KNeighborsClassifier(),
                    "Random Forest":RandomForestClassifier(),
                    "NaiveBayes":MultinomialNB(),
                    "Support vector":SVC(),
                    "GradientBoosting":GradientBoostingClassifier(),
                    
                }


                hyper_params={
                    "Logistic Regression":{
                        'penalty':config['Model_Hyperparameter']['Logistic_regression']['penalty'],
                        'solver':config['Model_Hyperparameter']['Logistic_regression']['solver'],
                    },
                    "Knearest neighbor":{
                        'n_neighbors':config['Model_Hyperparameter']['knearest_neighbor']['n_neighbors'],
                        'algorithm':config['Model_Hyperparameter']['knearest_neighbor']['algorithm'],
                    },
                    "Random Forest":{
                        'n_estimators':config['Model_Hyperparameter']['RandomForest']['n_estimators'],
                        'criterion':config['Model_Hyperparameter']['RandomForest']['criterion'],
                        'max_depth':config['Model_Hyperparameter']['RandomForest']['max_depth'],
                        'min_samples_split':config['Model_Hyperparameter']['RandomForest']['min_samples_split'],
                        'min_samples_leaf':config['Model_Hyperparameter']['RandomForest']['min_samples_leaf'],
                        'max_features':config['Model_Hyperparameter']['RandomForest']['max_features'],
                    },
                    "NaiveBayes":{
                        'alpha':config['Model_Hyperparameter']['NaiveBays']['alpha'],
                    },
                    "Support vector":{
                        'C':config['Model_Hyperparameter']['SupportVector']['C'],
                        'Kernal':config['Model_Hyperparameter']['SupportVector']['Kernal'],
                        'gamma':config['Model_Hyperparameter']['SupportVector']['gamma'],
                    },
                    "GradientBoosting":{
                        'loss':config['Model_Hyperparameter']['GradientBoosting']['loss'],
                        'learning_rate':config['Model_Hyperparameter']['GradientBoosting']['learning_rate'],
                        'n_estimators':config['Model_Hyperparameter']['GradientBoosting']['n_estimators'],
                        'criterion':config['Model_Hyperparameter']['GradientBoosting']['criterion'],
                        'max_depth':config['Model_Hyperparameter']['GradientBoosting']['max_depth'],
                        'max_features':config['Model_Hyperparameter']['GradientBoosting']['max_features'],
                    }
                }

                model_report:dict=model_evaluation(X_train=X_train,y_train=y_train,
                                                   X_test=X_test,y_test=y_test,models=Models,hyperparameter=hyper_params)
                logging.info('getting best model score')
                best_model_score=max(sorted(model_report.values()))


                best_model_name=list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]
                best_model=Models[best_model_name]

                if best_model_score<0.7:
                    raise CustomException("Best Model not found")
                logging.info("Best found model on both training and testing dataset:{best_model_name_lst} with accuracy:{model_score}".format(best_model_name_lst=best_model,model_score=best_model_score))


                save_obj(file_path=config['Artifacts_root']['model_obj'],
                         obj=best_model)

                

        except Exception as e:
            raise CustomException(e,sys)
