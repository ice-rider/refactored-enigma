
from threading import Thread
from app import run_scheduler, app


if __name__ == "__main__":
    scheduler_thread = Thread(target=run_scheduler, kwargs={"_app": app})
    scheduler_thread.start()
    app.run(port=5000)