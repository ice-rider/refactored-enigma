from ..models import UserModel
from .api import BaseResource



class UserResource(BaseResource):
    path = "/user/<int:user_id>"

    def get(self, user_id: int):
        user = UserModel.get_by_id(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user