import time

import schedule

from ..models import RoomModel

from .cian_parser import parse as parse_cian
from .avito_parser import parse as parse_avito


def update_database():
    print("\n\n= = = PARSING STARTED = = =")
    flats = parse_cian() + parse_avito()
    print("= = = PARSING FINISHED = = =\n\n")
    RoomModel.update_database(flats)


def job():
    update_database()


def run_scheduler():
    # initialize database
    update_database()

    # Schedule job to run every day at 10:00
    schedule.every().day.at("10:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)