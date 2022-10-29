from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class OneMinuteFraud(db.Model):
    id = db.Column(db.Integer, primary_key=True)