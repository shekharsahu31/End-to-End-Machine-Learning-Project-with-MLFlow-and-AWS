from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) # Data Classes are classes which are ony used for Storing varibles along with its data type.
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path