import os, sys
from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.logger import logging

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig) :
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e.sys) from e