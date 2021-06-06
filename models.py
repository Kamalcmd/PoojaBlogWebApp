from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime(datetime.utcnow))
    fname = db.Column('fName', db.String())
    lname = db.Column('lName', db.String())
    age= db.Column('Age', db.String())
    url = db.Column('URL', db.String())
    url_tag = db.Column('Alt Tag', db.String())


def __repr__(self):
    return f'''<portfolio (fName:{self.fname}
                    lName:{self.lname}
                    Age:{self.age}
                    URL: {self.url}
                    Alt Tag:{self.url_tag}
    )'''