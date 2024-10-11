from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager

from .api_logger import logger


api = Api(prefix="/api")
jwt = JWTManager()


def init_app(app: Flask) -> None:
    api.init_app(app)
    jwt.init_app(app)


class BaseResource(Resource):
    _docs = {}
    logger = logger
    path: str | None = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.path and isinstance(cls.path, str):
            api.add_resource(cls, cls.path)
        else:
            raise TypeError("class must have path property")
