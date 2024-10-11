import logging


logger = logging.getLogger("db_logger")  # take logger
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()  # console logger
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/db.log")  # file logger
file_handler.setLevel(logging.DEBUG)

# log format
date_format = "%d.%m.%y %H:%M"
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Database logger initialized successfully")