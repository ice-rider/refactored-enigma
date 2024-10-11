from flask import request

from ..models.room import RoomModel
from .utils import admin_access
from .api import BaseResource


class FlatListResource(BaseResource):
    path = "/flats/list/<str:random>"

    def get(self, random: str):
        rooms = RoomModel.get_all()
        return {
            "flats": [ room.json() for room in rooms ] if rooms else []
        }, 200
    

class FlatResource(BaseResource):
    path = "/flats/<int:id>"

    def get(self, id: int):
        room = RoomModel.get_by_url(id)
        return {
            "flat": room.json() if room else None
        }, 200
    

    @admin_access
    def patch(self, id: int):
        room = RoomModel.get_by_id(id)
        if not room:
            return {"message": "Flat not found"}, 404

        room.update_database([{
            "name": request.json["name"],
            "price": request.json["price"],
            "location": request.json["location"],
            "metrs": request.json["metrs"]
        }])
        return {
            "flat": room.json()
        }, 200
    

    @admin_access
    def delete(self, id: int):
        room = RoomModel.get_by_id(id)
        if not room:
            return {"message": "Flat not found"}, 404
        room.delete()
        return {"message": "Flat deleted"}, 200
