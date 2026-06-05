# app.py


from flask import Flask, render_template, redirect, url_for, session, request
from create_db import create_db
from models import db, Game,GameMobale,GamePC


app = Flask(__name__)

# --- КОНФІГУРАЦІЯ FLASK ---
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# --- МАРШРУТИ (ROUTES) ---

@app.route('/')
def home():
    """
    Головна сторінка додатку.
    """
    Games = Game.query.all()
    GameMobales = GameMobale.query.all()
    GamePCs = GamePC.query.all()

    return render_template('index.html', Games=Games, GameMobales=GameMobales, GamePCs=GamePCs)







# --- ЗАПУСК ДОДАТКА ---
if __name__ == '__main__':
    # create_db()
    app.run(debug=True)
