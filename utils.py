import json

filename_users = 'filesJson/users.json'
filename_orders = 'filesJson/orders.json'
filename_offers = 'filesJson/offers.json'


def load_user_from_json():  # загружает пользователей из файла
    with open(filename_users, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_users_from_json(users):  # сохраняет список словарей в json-файл
    with open(filename_users, 'w', encoding="utf-8") as file:
        json.dump(users, file, encure_ascii=False)


def load_orders_from_json():  # загружает заказы из файла
    with open(filename_orders, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_orders_from_json(orders):  # сохраняет список словарей в json-файл
    with open(filename_orders, 'w', encoding="utf-8") as file:
        json.dump(orders, file, encure_ascii=False)


def load_offers_from_json():  # загружает выполнение заказов из файла
    with open(filename_offers, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_offers_from_json(offers):  # сохраняет список словарей в json-файл
    with open(filename_offers, 'w', encoding="utf-8") as file:
        json.dump(offers, file, encure_ascii=False)


def get_all_users():  # все пользователи
    users = load_user_from_json()
    return users


def get_user_by_pk(pk):  # пользователь по id
    users = load_user_from_json()
    for user in users:
        if pk == user["id"]:
            return user


def add_user(user_data):  # записывает нового пользователя в файл user_data-словарь с данными пользователь
    users = load_user_from_json()
    last_user = users[-1] # user?
    last_id = last_user["id"]
    user_data["id"] = last_id + 1

    users.append(user_data)
    save_users_from_json(users)
    return user_data


def update_user(user_id, user_data):  # обновляет пользователя с нужным user_id
    users = load_user_from_json()
    for user in users:
        if user["id"] == user_id:
            user.update(user_data)
            break
    save_users_from_json(users)


def delete_user(user_id):  # удаляет пользователя с нужным user_id
    users = load_user_from_json()
    for index, user in enumerate(users):
        if user["id"] == user_id:
            del users[index]
            break
    save_users_from_json(users)


def get_all_orders():  # все заказы
    orders = load_orders_from_json()
    return orders


def get_order_by_pk(pk):  # заказ по пк
    orders = load_orders_from_json()
    for order in orders:
        if pk == order["id"]:
            return order


def add_order(order_data):  # записывает новый заказ в файл user_data-словарь с данными пользователь
    orders = load_orders_from_json()
    last_order = orders[-1] # user?
    last_id = last_order["id"]
    order_data["id"] = last_id + 1

    orders.append(order_data)
    save_orders_from_json(orders)
    return order_data


def update_order(order_id, order_data):  # обновляет заказ с нужным user_id
    orders = load_orders_from_json()
    for order in orders:
        if order["id"] == order_id:
            order.update(order_data)
            break
    save_orders_from_json(orders)


def delete_order(order_id):  # удаляет заказ с нужным user_id
    orders = load_user_from_json()
    for index, order in enumerate(orders):
        if order["id"] == order_id:
            del orders[index]
            break
    save_orders_from_json(orders)


def get_all_offers():  # все выполнение заказов
    offers = load_offers_from_json()
    return offers


def get_offer_by_pk(pk):  # одно выполнение заказа по нк
    offers = load_offers_from_json()
    for offer in offers:
        if pk == offer["id"]:
            return offer


def add_offer(offer_data):  # записывает нового выполнение заказа в файл user_data-словарь с данными пользователь
    offers = load_offers_from_json()
    last_offer = offers[-1] # user?
    last_id = last_offer["id"]
    offer_data["id"] = last_id + 1

    offers.append(offer_data)
    save_offers_from_json(offers)
    return offer_data


def update_offer(offer_id, offer_data):  # обновляет выполнение заказа с нужным user_id
    offers = load_offers_from_json()
    for offer in offers:
        if offer["id"] == offer_id:
            offer.update(offer_data)
            break
    save_offers_from_json(offers)


def delete_offer(offer_id):  # удаляет выполнение заказа с нужным user_id
    offers = load_offers_from_json()
    for index, offer in enumerate(offers):
        if offer["id"] == offer_id:
            del offers[index]
            break
    save_offers_from_json(offers)