from flask_sqlalchemy import SQLAlchemy

from utils.constants import env_const
from utils.decorators.singleton_decorator import Singleton

@Singleton
class ConnectionSqlServer():
    def __init__(self):
        user = env_const.DB_USER
        password = env_const.DB_PASSWORD
        host = env_const.DB_HOST
        port = env_const.DB_PORT
        schema = env_const.DB_SCHEMA
        self.conn_string = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{schema}?driver" \
                           f"=ODBC+Driver+17+for+SQL+Server"
        self.db = SQLAlchemy()
    
    def init_sql(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.conn_string
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db.init_app(app)

    
