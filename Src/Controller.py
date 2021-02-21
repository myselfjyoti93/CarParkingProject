#!/usr/bin/env python
from Config import SAMPLE_INPUT_FILE
from Config import SAMPLE_INPUT_FOLDER
from Src.Operations import Operations
from Lib.log_file import Logger
logger = Logger.get_logger()
import os

class Controller:
    operations_dict = {
        "Create_parking_lot" : Operations.create_parking_lot_wrapper,
        "Park" : Operations.park_wrapper,
        "Slot_numbers_for_driver_of_age" : Operations.slot_numbers_for_driver_of_age_wrapper,
        "Slot_number_for_car_with_number" : Operations.slot_number_for_car_with_number_wrapper,
        "Leave" : Operations.leave_wrapper,
        "Vehicle_registration_number_for_driver_of_age" : Operations.vehicle_registration_number_for_driver_of_age_wrapper
    }

    @staticmethod
    def parse_commands(command_string):
        commands = command_string.split(" ")
        Controller.operations_dict[commands[0]](commands[1:])

    @staticmethod
    def controller():
        try:
            folder_path = os.path.dirname(os.path.abspath(SAMPLE_INPUT_FOLDER))
            folder = os.path.join(folder_path, SAMPLE_INPUT_FOLDER)
            file = os.path.join(folder, SAMPLE_INPUT_FILE)
            file_input = open(file)
            for line in file_input:
                Controller.parse_commands(line.replace('\n', ''))
            file_input.close()
        except Exception as ex:
            logger.error(f"Exception raise {ex}")
