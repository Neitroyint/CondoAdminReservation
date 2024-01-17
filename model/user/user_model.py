from flask_sqlalchemy import SQLAlchemy

from db.connection_sqlserver import ConnectionSqlServer
from model.model_base import ModelBase

db_connection = ConnectionSqlServer.instance()
db: SQLAlchemy = db_connection.db

class User(ModelBase, db.Model):
    id_user = db.Column(db.Integer, primary_key=True)

    id_userinfo = db.Column(db.Integer, db.ForeignKey('userinfo.id_userinfo'), unique=True, nullable=True)
    userinfo = db.relationship('Userinfo', lazy=True, uselist=False)

    id_userstatus = db.Column(db.Integer, db.ForeignKey('userstatus.id_userstatus'), unique=True, nullable=False)
    userstatus = db.relationship('Userstatus', lazy=True, uselist=False)

    user_name = db.Column(db.String(80), unique=True, nullable=False)