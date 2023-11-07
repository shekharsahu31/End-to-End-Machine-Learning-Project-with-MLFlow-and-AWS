from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.entity.config_entity import DataValidationConfig
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.entity.config_entity import ModelTrainerConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath  = CONFIG_FILE_PATH, #CONFIG_FILE_PATH-> from constants > init.py , Contains address/ path to config yaml file
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath) #self.config -> config yaml file ka Data as Dict (Config Box Type ki)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root]) # using self.config.artifacts_root(key) -> value -  artifacts (making folder named 
                                                                                                             #artifacts in Current Dirctory)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        #config = self.config.data_ingestion

        create_directories([self.config.data_ingestion.root_dir]) # making directory - artifacts/data ingestion # will only create artifacts folder is not exist , If exist will be ignored.

        data_ingestion_config = DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir)

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir]) # artifacts/data_validation folder will be made.

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config