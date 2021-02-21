#!/usr/bin/env python
from Interfaces.Car import Car as CarInterface
from Lib.log_file import Logger
logger = Logger.get_logger()


class Car(CarInterface):
    def __init__(self):
        self.__car_no = None
        self.__driver_age = -1

    def get_car_num(self):
        if not self.__car_no:
            logger.info("No Car number is given")
            return None
        return self.__car_no

    def set_car_num(self, car_no):
        if not isinstance(car_no, str):
            logger.error(f"Invalid car no given : {car_no}")
            return False
        self.__car_no = car_no
        return True

    def get_driver_age(self):
        if self.__driver_age == -1:
            logger.error("Age is not provided for the driver")
            return -1
        return self.__driver_age

    def set_driver_age(self, age):
        if not isinstance(age, int):
            logger.error(f"Age value given is invalid {age}")
            return False
        self.__driver_age = age
        return True

