from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.dialects.sqlite import DATE
import uuid
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)


def get_user_id():
    return uuid.uuid4()


class MyCinema(db.Model):

    cine_id = db.Column(db.String(), primary_key=True, default=get_user_id())
    movie_name = db.Column(db.String())
    movie_date = db.Column(DATE())

    __tablename__ = "mycinema"

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    db.create_all()

