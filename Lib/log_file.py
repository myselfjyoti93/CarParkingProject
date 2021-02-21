#!/usr/bin/env python
import logging as logger
logger.basicConfig(level=logger.DEBUG, filename='.\Log\car_parking.log', format='%(asctime)s %(levelname)s:%(message)s')
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