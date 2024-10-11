import os
import datetime
import logging


date = datetime.datetime.now().strftime("%Y.%m.%d")

logger = logging.getLogger("api_logger")  # take logger
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()  # console logger
console_handler.setLevel(logging.DEBUG)

if not os.path.exists("logs"):
    os.mkdir("logs")

if not os.path.exists("logs/api"):
    os.mkdir("logs/api")

if not os.path.exists("logs/api_kafka_consumer"):
    os.mkdir("logs/api_kafka_consumer")

file_handler = logging.FileHandler("logs/api/%s.log" % (date,))  # file logger
file_handler.setLevel(logging.ERROR)

kafka_file_handler = logging.FileHandler("logs/api_kafka_consumer/%s.log" % (date,))
kafka_file_handler.setLevel(logging.INFO)

# log format
date_format = "%d.%m.%y %H:%M"
formatter = logging.Formatter("[%(asctime)s] %(name)s -> %(message)s", datefmt=date_format)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
kafka_file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(kafka_file_handler)

logger.info("loggers successfully initialized")