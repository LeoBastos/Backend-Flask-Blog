from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


#py -3 -m venv venvteste => Venv
#venvteste\Scripts\activate 
#pip install Flask
#set FLASK_APP=Nomeprojeto.py
#flask run
#set FLASK_DEBUG=1

app = Flask(__name__)
app.config['SECRET_KEY'] = '936f1d3ba27ae5bee1e99cf92ecaa426'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes