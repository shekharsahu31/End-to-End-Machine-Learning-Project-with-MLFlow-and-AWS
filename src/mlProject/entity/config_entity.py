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