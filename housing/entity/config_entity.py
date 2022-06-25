from collections import namedtuple
from unicodedata import name

# we are using namedtuple bcoz it provide all info inside any variable we create
# dictionary can do same but it is mutable 
# we dont want any one to alter our code once deployed.

DataIngestionConfig = namedtuple("DataIngestionConfig", 
["dataset_download_url", "tgz_download_dir", "raw_data_dir", "ingested_train__dir", "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
"transformed_train_dir", "transformed_test_dir", "preprocessed_object_file_path"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig", ["trained_model_file_path", "base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path", "time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])
