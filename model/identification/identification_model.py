from flask_sqlalchemy import SQLAlchemy

from db.connection_sqlserver import ConnectionSqlServer
from model.model_base import ModelBase

db_connection = ConnectionSqlServer.instance()
db: SQLAlchemy = db_connection.db

class Identification(ModelBase, db.Model):
    id_identification = db.Column(db.Integer, primary_key=True)
    id_identtype = db.Column(db.Integer, db.ForeignKey('identificationtype.id_identtype'), nullable=False)
    identificationtype = db.relationship('Identificationtype', lazy=True, uselist=False)
    identnumber = db.Column(db.String(255), unique=True, nullable=False)

        
    