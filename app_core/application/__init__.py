from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv
from sqlalchemy.orm import relationship


#create application
app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
#app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:root@host/database_name"
#app.config["SECRET_KEY"] = getenv("SECRET_KEY")
# set up database
db = SQLAlchemy(app)

from application import routes

# create the static database values 




