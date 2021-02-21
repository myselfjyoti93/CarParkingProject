#!/usr/bin/env python

from Lib.log_file import Logger
from Src.ParkingSlot import ParkingSlot
from Src.Car import Car

logger = Logger.get_logger()


class Operations:
    parking_lot_created = False
    parking_lot = None
    car_dict = {}

    @staticmethod
    def create_parking_lot_wrapper(args):
        if len(args) != 1:
            logger.error("invalid arguments")
            return False
        Operations.__create_parking_lot(int(args[0]))
        return True

    @staticmethod
    def __create_parking_lot(lot_size):
        if Operations.parking_lot_created:
            msg = "Parking Lot has already been created"
            logger.error(msg)
            print(msg)
            return None
        if not isinstance(lot_size, int):
            logger.error("lot size cannot be an integer")
            return None
        parking_lot = ParkingSlot()
        parking_lot.set_number_of_slots(lot_size)
        Operations.parking_lot_created = True
        Operations.parking_lot = parking_lot
        msg = f"Created parking of {lot_size} slots"
        print(msg)
        logger.info(msg)
        return parking_lot

    @staticmethod
    def park_wrapper(args):
        if len(args) != 3:
            logger.error("invalid arguments")
            return False
        Operations.__park(args[0], int(args[2]))
        return True

    @staticmethod
    def __park(vehicle_no, driver_age):
        if not Operations.parking_lot_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(vehicle_no, str):
            logger.error("vehicle no should be a string")
            return False
        if not isinstance(driver_age, int):
            logger.error("driver age should be an Integer")
            return False
        if vehicle_no in Operations.car_dict:
            msg = f"Vehicle {vehicle_no} already present in the parking lot"
            print(msg)
            logger.error(msg)
            return False
        car_obj = Car()
        car_obj.set_car_num(vehicle_no)
        car_obj.set_driver_age(driver_age)
        to_be_assigned_slot = Operations.parking_lot.get_slot_from_slots()
        if to_be_assigned_slot < 1:
            msg = f"Car with Vehicle registration number {vehicle_no} cannot be parked, as all slots are full"
            logger.error(msg)
            print(msg)
            return False
        Operations.car_dict[vehicle_no] = (car_obj, to_be_assigned_slot)
        Operations.parking_lot.assign_slot(to_be_assigned_slot, vehicle_no)
        msg = f"Car with Vehicle registration number {vehicle_no} has been parked at slot number {to_be_assigned_slot}"
        logger.info(msg)
        print(msg)
        return True

    @staticmethod
    def slot_numbers_for_driver_of_age_wrapper(args):
        if len(args) != 1:
            logger.error("invalid arguments")
            return False
        Operations.slot_numbers_for_driver_of_age(int(args[0]))
        return True

    @staticmethod
    def slot_numbers_for_driver_of_age(age):
        if not Operations.parking_lot_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(age, int):
            logger.error("vehicle no should be a string")
            return False
        slot_numbers = []
        for vehicle_info in Operations.car_dict:
            car_obj = Operations.car_dict[vehicle_info][0]
            car_obj_age = car_obj.get_driver_age()
            if car_obj_age == age:
                slot_numbers.append(str(Operations.car_dict[vehicle_info][1]))
        slot_numbers = ",".join(slot_numbers)
        if not slot_numbers:
            msg = f"No vehicle is parked with driver age {age}"
            print(msg)
            logger.error(msg)
            return False
        print(slot_numbers)
        return True

    @staticmethod
    def slot_number_for_car_with_number_wrapper(args):
        if len(args) != 1:
            logger.error("invalid arguments")
            return False
        Operations.__slot_number_for_car_with_number(args[0])
        return True

    @staticmethod
    def __slot_number_for_car_with_number(vehicle_no):
        if not Operations.parking_lot_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(vehicle_no, str):
            return False
        if vehicle_no not in Operations.car_dict.keys():
            msg = f"Vehicle {vehicle_no} not present in parking lot"
            print(msg)
            logger.error(msg)
            return False
        slot_no = Operations.car_dict[vehicle_no][1]
        print(slot_no)
        return True

    @staticmethod
    def leave_wrapper(args):
        if len(args) != 1:
            logger.error("invalid arguments")
            return False
        Operations.__leave(int(args[0]))
        return False

    @staticmethod
    def __leave(slot_no):
        if not Operations.parking_lot_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(slot_no, int):
            logger.error("Slot number should be an integer")
            return False
        if Operations.parking_lot.get_parking_lot_capacity() < slot_no:
            msg = f"slot no {slot_no} not in Parking lot capacity"
            logger.error(msg)
            print(msg)
            return False
        if not Operations.parking_lot.get_slot_info(slot_no):
            return False
        car_no_in_slot = Operations.parking_lot.get_slot_info(slot_no)
        Operations.parking_lot.remove_slot(slot_no)
        age_of_driver_left = Operations.car_dict[car_no_in_slot][0].get_driver_age()
        del Operations.car_dict[car_no_in_slot]
        Operations.parking_lot.reallocate_slot_into_slots(slot_no)
        msg = f"Slot number {slot_no} vacated, the car with vehicle registration number {car_no_in_slot} left the place," \
              f"the driver of the car was of the age {age_of_driver_left}"
        print(msg)
        logger.info(msg)
        return True

    @staticmethod
    def vehicle_registration_number_for_driver_of_age_wrapper(args):
        if len(args) != 1:
            logger.error("invalid arguments")
            return False
        Operations.__vehicle_registration_number_for_driver_of_age(int(args[0]))
        return True

    @staticmethod
    def __vehicle_registration_number_for_driver_of_age(age):
        if not Operations.parking_lot_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(age, int):
            logger.error("age should be an integer")
            return False
        vehicle_registration_numbers = []
        for vehicle_info in Operations.car_dict:
            car_obj = Operations.car_dict[vehicle_info][0]
            car_obj_age = car_obj.get_driver_age()
            if car_obj_age == age:
                vehicle_registration_numbers.append(vehicle_info)
        vehicle_registration_numbers = ",".join(vehicle_registration_numbers)
        print("null" if not vehicle_registration_numbers else vehicle_registration_numbers)
        return True
