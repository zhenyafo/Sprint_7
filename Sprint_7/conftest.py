import pytest
import requests
from utils.helpers import register_new_courier_and_return_login_password, delete_courier


@pytest.fixture
def base_url():
    return "https://qa-scooter.praktikum-services.ru"


@pytest.fixture
def create_and_delete_courier():
    courier_data = register_new_courier_and_return_login_password()
    login = courier_data[0]
    password = courier_data[1]
    first_name = courier_data[2]
    
    yield login, password, first_name
    
    response = requests.post(
        f"https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
        data={"login": login, "password": password}
    )
    if response.status_code == 200:
        courier_id = response.json()["id"]
        delete_courier(courier_id)


@pytest.fixture
def get_courier_id(create_and_delete_courier):
    login, password, _ = create_and_delete_courier
    
    response = requests.post(
        f"https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
        data={"login": login, "password": password}
    )
    return response.json()["id"] 