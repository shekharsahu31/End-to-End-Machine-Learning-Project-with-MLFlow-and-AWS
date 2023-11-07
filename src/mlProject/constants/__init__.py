# This constans > init.py is used for storing the path of yaml files to a variables using PATH function which handles diff. OS based change
# in path style like in linux / is used and in windows \ is used. 


from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")