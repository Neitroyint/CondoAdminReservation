from flask_sqlalchemy import SQLAlchemy

from db.connection_sqlserver import ConnectionSqlServer
from model.model_base import ModelBase

db_connection = ConnectionSqlServer.instance()
db: SQLAlchemy = db_connection.db

class Userinfo(ModelBase, db.Model):
    id_userinfo = db.Column(db.Integer, primary_key=True)
    id_identification = db.Column(db.Integer, db.ForeignKey('identification.id_identification'), unique=True, nullable=False)

    identification = db.relationship('Identification', lazy=True, uselist=False)

    name = db.Column(db.String(255), nullable=False)
    last_name_1 = db.Column(db.String(255), nullable=False)
    last_name_2 = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Integer, nullable=True)
