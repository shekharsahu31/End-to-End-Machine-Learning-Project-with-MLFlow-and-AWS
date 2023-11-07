from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # Data Classes are classes which are ony used for Storing varibles along with its data type.
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict # to store data of schema.yaml file we are using this extra variable , other all are to store PATHs    



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path #from config.yaml
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float    #from params.yaml
    l1_ratio: float
    target_column: str  #from schema.yaml    