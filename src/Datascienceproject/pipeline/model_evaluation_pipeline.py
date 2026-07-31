
from src.Datascienceproject.config.configuration import ConfigurationManager
from src.Datascienceproject.components.model_evaluation import ModelEvaluation
from src.Datascienceproject import logger


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_trainer = config.get_model_evaluation()
        model_trainer = ModelEvaluation(config=model_evaluation_trainer)
        model_trainer.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
