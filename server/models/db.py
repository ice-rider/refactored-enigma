from flask_sqlalchemy import SQLAlchemy

from flask.typing import AppOrBlueprintKey

from .user import UserModel


db = SQLAlchemy()


def init_app(app: AppOrBlueprintKey) -> None:
    global db, db_logger

    db.init_app(app)
    with app.app_context():
        db.create_all()

        superuser = UserModel(
            username="admin",
            email="admin",
            password="admin",
            system=True
        )
        superuser.save()
        db_logger.info("Database initialized successfully")


class BaseModel(db.Model):  # type: ignore
    __abstract__ = True

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