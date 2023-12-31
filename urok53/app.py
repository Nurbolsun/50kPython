from flask import Flask, render_template, request
from database import Good, engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Session = sessionmaker(engine)

@app.route("/")
def homepage():
    session = Session()
    goods = session.query(Good)
    session.commit()

    f = open("goods.txt", "r", encoding="utf-8")
    txt = f.readlines()
    return render_template("index.html", goods = goods)

@app.route("/add/", methods=["POST"])
def add():
    good = request.form["good"]

    session = Session()
    good_obj = Good(name=good)
    session.add(good_obj)
    session.commit()

    return """
        <h1>Инвентарь пополнен!</h1>
        <a href="/"> Домой </a>
    """