# End-to-End-Machine-Learning-Project-with-MLFlow-and-AWS

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/shekharsahu31/End-to-End-Machine-Learning-Project-with-MLFlow-and-AWS
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/shekharsahu31/End-to-End-Machine-Learning-Project-with-MLFlow-and-AWS.mlflow \
MLFLOW_TRACKING_USERNAME=shekharsahu31 \
MLFLOW_TRACKING_PASSWORD=0cb0eedf039cf572be06483551f8be77d1e00124 \
python script.py

Run this to export as env variables in git bash :

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/shekharsahu31/End-to-End-Machine-Learning-Project-with-MLFlow-and-AWS.mlflow 

export MLFLOW_TRACKING_USERNAME=shekharsahu31 

export MLFLOW_TRACKING_PASSWORD=0cb0eedf039cf572be06483551f8be77d1e00124

```