from flask_restful import Api

from db.connection_sqlserver import ConnectionSqlServer
from model.marshmallow_init import MarshmallowInit
from service.endpoint.endpoint_service import add_endpoints
from service.flask_init.flask_init_service import FlaskInit
from utils.constants import env_const

app = (FlaskInit.instance()).app

#Initialize database
db = ConnectionSqlServer.instance()
db.init_sql(app)

#Initialize Marshmallow
ma = MarshmallowInit.instance()
ma.init_ma(app)

#Initialize api
api = Api(app)
add_endpoints(api)

if __name__ == '__main__':
    app.run(host=env_const.APIHOST, port=env_const.APIPORT)
