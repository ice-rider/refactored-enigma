from __future__ import annotations

from enum import Enum
from typing import TypeAlias, Literal

from passlib.hash import pbkdf2_sha256

from .db import db, BaseModel


USER_ROLE: TypeAlias = Literal["admin", "user"]


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"


class UserModel(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(87))
    confirmed = db.Column(db.Boolean, default=False)
    code = db.relationship("CodeModel", backref="user", uselist=False)
    _role = db.Column(db.Enum(UserRole), default=UserRole.USER)

    def __init__(self, username: str, email: str, password: str, system: bool = False):
        conflict_user = self.get_by_email(email)
        self.logger.info(conflict_user)
        if conflict_user:
            raise Exception(f"User {conflict_user} already registered")
        password_hash: str = pbkdf2_sha256.hash(password)
        # set fields after validate
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = UserRole.ADMIN if system else UserRole.USER

    def json(self) -> dict[str, int | str]:
        return {
            "id": self.id,
            "username": self.username,
            "verified": self.confirmed,
            "role": self.role
        }
    
    def confirm_code(self, code) -> bool:
        return self.code.check(code)

    @classmethod
    def get_by_email(cls, _email) -> UserModel | None:
        return cls.query.filter_by(email=_email).first()
    
    @classmethod
    def authorize(cls, _email: str, password: str) -> UserModel | None:
        cls.logger.info("authorizing user: " + _email + " " + password)
        user: UserModel = cls.get_by_email(_email)
        cls.logger.info(user)
        
        if not user:
            return None
        
        if pbkdf2_sha256.verify(password, user.password_hash):
            return user
        else:
            return None

    @property
    def role(self) -> str:
        return self._role.value
    
    @role.setter
    def role(self, value: USER_ROLE):
        try:
            self._role = UserRole(value)
        except ValueError as e:
            raise ValueError("invalid user role") from e

    def change_role(self, _role: USER_ROLE | UserRole):
        if isinstance(_role, UserRole):
            self._role = _role
        else:
            try:
                self.role = _role
            except ValueError as e:
                raise Exception(f"can't set user role={_role}") from e

    def __repr__(self) -> str:
        return f"<User {self.username}>"