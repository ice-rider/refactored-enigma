import random
import string

from flask_sqlalchemy import SQLAlchemy
from flask.typing import AppOrBlueprintKey
from passlib.hash import pbkdf2_sha256

from .db_logger import logger as db_logger


db = SQLAlchemy()


def init_app(app: AppOrBlueprintKey) -> None:
    global db, db_logger

    db.init_app(app)
    with app.app_context():
        db.create_all()
        password = "".join(random.choices(string.ascii_letters + string.digits, k=16))

        from .user import UserModel
        superuser = UserModel(
            "admin", "admin@email.com", password, system=True
        )
        superuser.save()
        db_logger.info(f"Superuser created: \n\temail = admin@email.com; {password = }; username = admin")
        db_logger.info("Database initialized successfully")


class BaseModel(db.Model):  # type: ignore
    __abstract__ = True
    logger = db_logger

    def __str__(self) -> str:
        return str(self.json())

    @classmethod
    def get_by_id(cls, id: int):
        return cls.query.get(id)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()