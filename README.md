# End to End Data Science Project

<!-- Extreme modular coding -->
how we can specifically use classes


### Workflow -- ML Pipeline

1. Data ingestion  -> database(mysql/mongo DB) or API basically a ETL pipeline
2. Data Validation -> schema should be validated 
3. Data Transformation -> Feature engineering or data preprocessing
4. Model Trainer -> elastic net
5. Model Evalution -> MLFLOW & Dagshub

Dagshub -> is the remote repository to track each and everything like data versioning, model versioning 
MLflow -> experiment tracking 


## Workflows

1. Update config.yaml --> data souce input where i'm taking the data how i will be ingestion
2. Update schema.yaml --> Data validation
3. Update params.yaml -> parameter
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline -> training pipeline & batch prediction pipeline
8. Update the main.py


artifacts/
  data_ingestion/        → output of data ingestion step (raw data)
  data_transformation/   → output of transformation step (train.csv, test.csv)
  data_validation/       → output of validation step (status.txt)
  model_evaluation/      → output of evaluation step (metrics.json)
  model_trainer/         → output of training step (model.pkl)

in each stages we have modules

confitguration
components
pipeline

for the refective stages like ...

idea is to write and  implement modular statruture 

what is the use of particing this modular coding
readability and incase of any changes like ...


what is elastic net and paramter used 

joblib


we should know what we do in each stage

