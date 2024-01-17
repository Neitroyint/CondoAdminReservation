from db.connection_sqlserver import ConnectionSqlServer

from flask_sqlalchemy import SQLAlchemy

from model.model_base import ModelBase

db_connection = ConnectionSqlServer.instance()
db: SQLAlchemy = db_connection.db

class Identificationtype(ModelBase, db.Model):
    id_identtype = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    