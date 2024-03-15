from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app =Flask(__name__) 

app.config["SECRET_KEY"] ='9ab622881a119dadd6df2ca5'
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///data.db'
app.config["SQLALCHEMY_MODIFICATION_TRACK"]= False 


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from main import route