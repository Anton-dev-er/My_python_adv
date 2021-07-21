from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from envparse import Env

env = Env()
DB_URL = env.str("DB_URL")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)


class UsersData(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(100), nullable=False, unique=True)
    chat_id = db.Column(db.Integer, nullable=False)
    create_dt = db.Column(db.DateTime, default=datetime.utcnow())


if __name__ == "__main__":
    print([i.nickname for i in UsersData.query.all()])
