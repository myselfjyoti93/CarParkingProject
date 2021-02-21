#!/usr/bin/env python
from Interfaces.ParkingSlot import ParkingSlot as ParkingSlotInterface
from Lib.log_file import Logger
import heapq

logger = Logger.get_logger()


class ParkingSlot(ParkingSlotInterface):
    def __init__(self):
        self.__num_of_slots = 0
        self.__num_of_slots_available = 0
        self.__available_slot_numbers = []
        self.__slot_info = {}
        self.__slots_created = False

    def get_parking_lot_capacity(self):
        return self.__num_of_slots

    def get_number_of_slots(self):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return -1
        return self.__num_of_slots

    def set_number_of_slots(self, number):
        if self.__slots_created:
            logger.error("Parking Lot already created yet")
            return False
        if not isinstance(number, int):
            logger.error("Slot should be an Integer")
            return False
        self.__num_of_slots = number
        self.__num_of_slots_available = self.__num_of_slots
        self.__available_slot_numbers = [i for i in range(1, self.__num_of_slots+1)]
        self.__slots_created = True
        logger.info(f"Parking lot created, Total slots : {self.__num_of_slots}")
        logger.info(f"Available slots : {self.__available_slot_numbers}")
        return True

    def get_slot_from_slots(self):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return -1
        if not self.__has_slot_reached_min():
            heapq.heapify(self.__available_slot_numbers)
            slot_no = heapq.heappop(self.__available_slot_numbers)
            self.__num_of_slots_available = self.__num_of_slots_available - 1
            return slot_no
        logger.error("All slots occupied. Please wait")
        return -1

    def reallocate_slot_into_slots(self, slot_no):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(slot_no, int):
            return False
        if not self.__has_slot_reached_max():
            heapq.heapify(self.__available_slot_numbers)
            heapq.heappush(self.__available_slot_numbers, slot_no)
            self.__num_of_slots_available = self.__num_of_slots_available + 1
            return True
        logger.error("Slot Size has reached its threshold")
        return False

    def __has_slot_reached_max(self):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return False
        return True if self.__num_of_slots_available == self.__num_of_slots else False

    def __has_slot_reached_min(self):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return False
        return True if self.__num_of_slots_available == 0 else False

    def assign_slot(self, slot_no, car_no):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(slot_no, int) and not isinstance(car_no, str):
            return False
        self.__slot_info[slot_no] = car_no
        logger.info(f"car {car_no} assigned to {slot_no}")
        return True

    def get_slot_info(self, slot_no):
        if not self.__slots_created:
            msg = "No Parking Lot created yet"
            logger.error(msg)
            print(msg)
            return None
        if not isinstance(slot_no, int):
            msg = "slot number not an integer"
            print(msg)
            logger.error(msg)
            return None
        if slot_no not in self.__slot_info.keys():
            msg = f"no vehicle is assigned to slot : {slot_no}"
            print(msg)
            logger.error(msg)
            return None
        return self.__slot_info[slot_no]

    def remove_slot(self, slot_no):
        if not self.__slots_created:
            logger.error("No Parking Lot created yet")
            return False
        if not isinstance(slot_no, int):
            logger.error("slot no should be an integer")
            return False
        del self.__slot_info[slot_no]
        logger.info(f"slot no {slot_no} removed")
        return True
