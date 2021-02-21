#!/usr/bin/env python
import logging as logger
import os
log_folder_path = os.path.dirname(os.path.abspath("Log"))
log_folder = os.path.join(log_folder_path, "Log")
log_file = os.path.join(log_folder, "car_parking.log")

logger.basicConfig(level=logger.DEBUG, filename=log_file, format='%(asctime)s %(levelname)s:%(message)s')
logger = logger
class Logger:

    __instance = None
    @staticmethod
    def get_logger():
        if Logger.__instance is None:
            Logger.__instance = logger
        return Logger.__instance

    def __init__(self):
        raise RuntimeError('Call get_logger() instead')