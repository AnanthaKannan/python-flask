from .db import db

class Admin(db.Document):
    name = db.StringField(required=True, unique=True)
    address = db.StringField(required=True)
    age = db.IntField(min_value=18, max_value=60, required=True)