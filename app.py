from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

import utils
from utils import get_all_users, get_user_by_pk, get_all_orders, get_order_by_pk, get_all_offers, get_offer_by_pk

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///homework16.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)  # должность
    phone = db.Column(db.String)


class Offer(db.Model):  # Предложение/ скидка
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    executor_id = db.Column(db.Integer, db.ForeignKey("User.id"))  # исполнитель
    order_id = db.Column(db.Integer, db.ForeignKey("Order.id"))  # номер заказа

    orders = relationship("Order")
    user = relationship("User")


class Order(db.Model):  # заказ
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)  # описание
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("User.id"))  # покупатель
    executor_id = db.Column(db.Integer, db.ForeignKey("Offer.id"))  # исполнитель

    user = relationship("User")
    offers = relationship("Offer")


with app.app_context():
    db.create_all()


@app.route("/users")
def get_all_users_page():
    data = get_all_users()
    return jsonify(data)


@app.route("/users/<int:pk>")
def get_user_by_pk_page(pk):
    user = get_user_by_pk(pk)
    return jsonify(user)


# Реализуйте создание пользователя user посредством метода POST на URL /users  для users.
@app.route("/users", methods=['POST'])
def create_user_page():
    user = {}
    post_data = request.json

    user["id"] = post_data.get("id")
    user["first_name"] = post_data.get("first_name")
    user["last_name"] = post_data.get("last_name")
    user["age"] = post_data.get("age")
    user["email"] = post_data.get("email")
    user["role"] = post_data.get("role")
    user["phone"] = post_data.get("phone")

    user_created = utils.add_user(user)  # записывает нового пользователя в файл user_data-словарь с данными
    return jsonify(user_created)


# обновление пользователя user посредством метода PUT на URL /users/<id>  для users.
# В Body будет приходить JSON со всеми полями для обновление заказа.
@app.route("/users/<int:pk>", methods=['PUT'])
def update_user_page(pk):
    user = get_user_by_pk(pk)
    post_data = request.json

    user["id"] = post_data.get("id")
    user["first_name"] = post_data.get("first_name")
    user["last_name"] = post_data.get("last_name")
    user["age"] = post_data.get("age")
    user["email"] = post_data.get("email")
    user["role"] = post_data.get("role")
    user["phone"] = post_data.get("phone")

    user_update = utils.update_user(pk, user)  # обновляет пользователя с нужным user_id

    return jsonify(user_update)


# удаление пользователя user посредством метода DELETE на URL /users/<id> для users.
@app.route("/users/<int:pk>", methods=['DELETE'])
def delete_user_page(pk):
    utils.delete_user(pk)  # удаляет пользователя с нужным user_id
    return ""


@app.route("/orders")
def get_all_orders_page():
    data = get_all_orders()
    return jsonify(data)


@app.route("/orders/<int:pk>")
def get_order_by_pk_page(pk):
    order = get_order_by_pk(pk)
    return jsonify(order)


# Реализуйте создание пользователя user посредством метода POST на URL /users  для users.
@app.route("/orders", methods=['POST'])
def create_order_page():
    order = {}
    post_data = request.json

    order["id"] = post_data.get("id")
    order["name"] = post_data.get("name")
    order["description"] = post_data.get("description")
    order["start_date"] = post_data.get("start_date")
    order["end_date"] = post_data.get("end_date")
    order["address"] = post_data.get("address")
    order["price"] = post_data.get("price")
    order["customer_id"] = post_data.get("customer_id")
    order["executor_id"] = post_data.get("executor_id")

    order_created = utils.add_order(order)  # записывает нового пользователя в файл user_data-словарь с данными
    return jsonify(order_created)


# обновление пользователя user посредством метода PUT на URL /users/<id>  для users.
# В Body будет приходить JSON со всеми полями для обновление заказа.
@app.route("/orders/<int:pk>", methods=['PUT'])
def update_order_page(pk):
    order = get_order_by_pk(pk)
    post_data = request.json

    order["id"] = post_data.get("id")
    order["name"] = post_data.get("name")
    order["description"] = post_data.get("description")
    order["start_date"] = post_data.get("start_date")
    order["end_date"] = post_data.get("end_date")
    order["address"] = post_data.get("address")
    order["price"] = post_data.get("price")
    order["customer_id"] = post_data.get("customer_id")
    order["executor_id"] = post_data.get("executor_id")

    order_update = utils.update_order(pk, order)  # обновляет пользователя с нужным user_id

    return jsonify(order_update)


# удаление пользователя user посредством метода DELETE на URL /users/<id> для users.
@app.route("/orders/<int:pk>", methods=['DELETE'])
def delete_order_page(pk):
    utils.delete_order(pk)  # удаляет пользователя с нужным user_id
    return ""


@app.route("/offers")
def get_all_offers_page():
    offers = get_all_offers()
    return jsonify(offers)


@app.route("/offers/<int:pk>")
def get_offer_by_pk_page(pk):
    offer = get_offer_by_pk(pk)
    return jsonify(offer)


# Реализуйте создание пользователя user посредством метода POST на URL /users  для users.
@app.route("/offers", methods=['POST'])
def create_offer_page():
    offer = {}
    post_data = request.json

    offer["id"] = post_data.get("id")
    offer["order_id"] = post_data.get("order_id")
    offer["executor_id"] = post_data.get("executor_id")

    offer_created = utils.add_offer(offer)  # записывает нового пользователя в файл user_data-словарь с данными
    return jsonify(offer_created)


# обновление пользователя user посредством метода PUT на URL /users/<id>  для users.
# В Body будет приходить JSON со всеми полями для обновление заказа.
@app.route("/offers/<int:pk>", methods=['PUT'])
def update_offer_page(pk):
    offer = get_offer_by_pk(pk)
    post_data = request.json

    offer["id"] = post_data.get("id")
    offer["order_id"] = post_data.get("order_id")
    offer["executor_id"] = post_data.get("executor_id")

    offer_update = utils.update_offer(pk, offer)  # обновляет пользователя с нужным user_id

    return jsonify(offer_update)


# удаление пользователя user посредством метода DELETE на URL /users/<id> для users.
@app.route("/offers/<int:pk>", methods=['DELETE'])
def delete_offer_page(pk):
    utils.delete_offer(pk)  # удаляет пользователя с нужным user_id
    return ""


if __name__ == '__main__':
    app.run(debug=True)
