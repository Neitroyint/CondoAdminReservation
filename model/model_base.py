from flask_sqlalchemy import SQLAlchemy

from db.connection_sqlserver import ConnectionSqlServer

db_connection = ConnectionSqlServer.instance()
db: SQLAlchemy = db_connection.db

class ModelBase:
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as exc:
            db.session.rollback()
            raise exc

    def update(self):
        try:
            db.session.commit()
        except Exception as exc:
            db.session.rollback()
            raise exc