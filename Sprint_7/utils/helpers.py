import requests
import random
import string
import allure
from data.constants import ORDER_DATA, BASE_URL
from utils.urls import get_create_courier_url, get_orders_url


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("Регистрация нового курьера")
def register_new_courier_and_return_login_password():
    login_pass = []
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(get_create_courier_url(), data=payload)
    
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    
    return login_pass


@allure.step("Удаление курьера по ID: {courier_id}")
def delete_courier(courier_id):
    from utils.urls import get_delete_courier_url
    response = requests.delete(get_delete_courier_url(courier_id))
    return response


@allure.step("Создание тестового заказа с цветом: {color}")
def create_test_order(color=None):
    payload = ORDER_DATA.copy()
    
    if color:
        if isinstance(color, list):
            payload["color"] = color
        else:
            payload["color"] = [color]
    
    response = requests.post(get_orders_url(), json=payload)
    
    return response


@allure.step("Создание курьера с данными: login={login}")
def create_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(get_create_courier_url(), data=payload)
    return response


@allure.step("Авторизация курьера: login={login}")
def login_courier(login, password):
    from utils.urls import get_login_courier_url
    response = requests.post(get_login_courier_url(), data={"login": login, "password": password})
    return response