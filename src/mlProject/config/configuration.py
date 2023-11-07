from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig

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

        create_directories([self.config.data_ingestion.root_dir]) # making directory - artifacts/data ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_URL=self.config.data_ingestion.source_URL,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir)

        return data_ingestion_config