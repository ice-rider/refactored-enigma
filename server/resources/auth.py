import string
import random

from flask import request
from flask_jwt_extended import create_access_token

from models import UserModel, CodeModel
from .api import BaseResource
from .utils import send_email


class LoginResource(BaseResource):
    path = "/login"

    def post(self):
        user = UserModel.authorize(request.json.get("email"), request.json.get("password"))
        if not user:
            return {"message": "User not found"}, 404
        access_token = create_access_token(identity=user.json())
        return {
            "access_token": access_token,
            "user": user.json()
        }, 200


class RegisterResource(BaseResource):
    path = "/register"

    def post(self):
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        if not all([username, email, password]):
            return {"message": "All fields are required"}, 400
        
        user = UserModel(username, email, password)
        user.save()

        code = "".join(random.choices(string.ascii_digits, k=6))
        user.code = CodeModel(code, user.id).save()

        access_token = create_access_token(identity=user.json())

        send_email(email, username, code)

        return {
            "access_token": access_token,
            "user": user.json()
        }, 201
