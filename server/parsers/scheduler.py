import time

import schedule

from models import RoomModel

from .cian_parser import parse as parse_cian
from .avito_parser import parse as parse_avito
from .parser_logger import logger as parser_logger


parser_logger.info("Scheduler initializing...")
app = None


def update_database():
    global app
    parser_logger.info("\n\n= = = PARSING STARTED = = =")
    flats = parse_avito() + parse_cian()
    parser_logger.info("= = = PARSING FINISHED = = =\n\n")
    with app.app_context():
        RoomModel.update_database(flats)


def job():
    update_database()


def run_scheduler(_app):
    global app
    app = _app

    parser_logger.info("Scheduler initialized successfully")
    parser_logger.info("Start parsing...")
    # initialize database
    update_database()

    # Schedule job to run every day at 10:00
    schedule.every().day.at("10:00").do(job)
    parser_logger.info("Scheduler started")
    while True:
        schedule.run_pending()
        time.sleep(1)