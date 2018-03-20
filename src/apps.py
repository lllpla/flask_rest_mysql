from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

DEV_FLAG = True
