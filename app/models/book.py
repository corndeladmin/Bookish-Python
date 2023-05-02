from dataclasses import dataclass
from app.models import db
from marshmallow import Schema, fields


class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
class BookSchema(Schema):
    id = fields.Int()
    title = fields.Str()