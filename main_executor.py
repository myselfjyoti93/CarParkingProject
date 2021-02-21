#!/usr/bin/env python
from Lib.log_file import Logger
log = Logger.get_logger()

import Src.Controller as Controller

if __name__ == "__main__":
    Controller.Controller.controller()