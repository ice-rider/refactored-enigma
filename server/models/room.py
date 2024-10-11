from __future__ import annotations

from .db import db, BaseModel


class RoomModel(BaseModel):
    __tablename__ = "room"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    metrs = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)

    def __init__(self, name: str, price: int, location: str, metrs: str, image: str, url: list[str], source: str):
        self.name = name
        self.price = price
        self.location = location
        self.metrs = metrs
        self.image = image
        self.url = "__".join(url)
        self.source = source

    def __init__(self, name: str):
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "location": self.location,
            "metrs": self.metrs,
            "image": self.image,
            "url": self.urla.split("__"),
            "source": self.source
        }
    
    @classmethod
    def get_by_url(cls, url: str) -> RoomModel | None:
        return cls.query.filter_by(url=url).first()

    @classmethod
    def update_database(cls, flats: list[dict]):
        for flat in flats:
            room = cls.get_by_url(flat["url"])
            if room:
                room.name = flat["name"]
                room.price = flat["price"]
                room.location = flat["location"]
                room.metrs = flat["metrs"]
                room.image = flat["image"]
                room.url = "__".join(flat["url"])
                room.source = flat["source"]
            else:
                new_room = cls(
                    name=flat["name"],
                    price=flat["price"],
                    location=flat["location"],
                    metrs=flat["metrs"],
                    image=flat["image"],
                    url=flat["url"],
                    source=flat["source"]
                )
                new_room.save()