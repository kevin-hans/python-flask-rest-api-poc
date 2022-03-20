from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Json
app.config['JSON_AS_ASCII'] = False

# DB
_db_user = os.environ.get("DB_USER", default="user")
_db_pass = os.environ.get("DB_PASS", default="pass")
_db_uri = os.environ.get("DB_URI", default="localhost")
_db_name = os.environ.get("DB_NAME", default="dbname")

_full_db_uri = 'postgresql://{0}:{1}@{2}/{3}'.format(_db_user, _db_pass, _db_uri, _db_name)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = _full_db_uri
db = SQLAlchemy(app)