import logging
from housing.pipeline.pipeline import Pipeline
from housing.component.data_transformation import DataTransformation
import os

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuartion().get_data_transformation_config()
        #print(data_validation_config)
        #schema_file_path = r"D:\GIT\project\ml_project\config\schema.yaml"
        #file_path = r"D:\GIT\project\ml_project\housing\artifact\data_ingestion\2022-07-07-23-00-13\ingested_data\train\housing.csv"
        #df = DataTransformation.get_data_transformer_object()
        #print(df.columns)
        #print(df.dtypes)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()