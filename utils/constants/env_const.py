import os

# API configuration
APIHOST = os.environ["USER_API_HOST"]
APIPORT = os.environ["USER_API_PORT"]
APIENDPOINT = os.environ["USER_API_ENDPOINT"]
IS_DEBUG = True

# Authentication
AUTH_URL = os.environ["AUTH_URL"]

# Database configuration
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_SCHEMA = os.environ["DB_SCHEMA"]