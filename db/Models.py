from .database import db
import mongoengine as me


class Tasks(db.Document):
    description = db.StringField(required=True)
    duration = db.IntField()
    recordedTime = db.IntField()
    status = db.BooleanField()
