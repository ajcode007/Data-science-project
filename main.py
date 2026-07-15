from src.Datascienceproject import logger
from src.Datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingesion = DataIngestionTrainingPipeline()
    data_ingesion.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


logger.info("Welcome to our custom logging data science")

