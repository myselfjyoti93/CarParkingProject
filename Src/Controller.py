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
            file_input = open(os.path.join(SAMPLE_INPUT_FOLDER, SAMPLE_INPUT_FILE))
            for line in file_input:
                Controller.parse_commands(line.replace('\n', ''))
        except Exception as ex:
            log(f"Exception raise {ex}")
        finally:
            file_input.close()
