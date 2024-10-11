import logging
import os
import datetime

date = datetime.datetime.now().strftime("%Y.%m.%d")

logger = logging.getLogger("parser_logger")  # take logger
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()  # console logger
console_handler.setLevel(logging.DEBUG)

if not os.path.exists("logs"):
    os.mkdir("logs")

if not os.path.exists("logs/parser"):
    os.mkdir("logs/parser")

file_handler = logging.FileHandler("logs/parser/%s.log" % (date,))  # file logger
file_handler.setLevel(logging.ERROR)

# log format
date_format = "%d.%m.%y %H:%M"
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Parser logger initialized successfully")
