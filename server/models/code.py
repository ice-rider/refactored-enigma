from .db import db, BaseModel


class CodeModel(BaseModel):
    __tablename__ = "code"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, code: str, user_id: int):
        self.code = code
        self.user_id = user_id

    def check(self, code: str) -> bool:
        return self.code == code