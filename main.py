
from income_inequality.logging import logger 
from income_inequality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from income_inequality.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from income_inequality.pipeline.stage_03_model_training import ModelTrainingPipeline
from income_inequality.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} Completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started <<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} Completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started <<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} Completed <<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>> Stage {STAGE_NAME} Started <<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} Completed <<<")
except Exception as e:
    logger.exception(e)
    raise e

