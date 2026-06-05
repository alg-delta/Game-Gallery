from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class  Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(230), nullable = True)
    link = db.Column(db.String(230), nullable=True)
    price = db.Column(db.Integer, nullable = False)
    image = db.Column(db.String(230), nullable = True)

class GameMobale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(230), nullable=True)
    link = db.Column(db.String(230), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(230), nullable=True)

class GamePC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(230), nullable=True)
    link = db.Column(db.String(230), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(230), nullable=True)



