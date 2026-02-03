import pytest
import allure
import requests
from utils.helpers import register_new_courier_and_return_login_password
from utils.urls import get_login_courier_url, get_delete_courier_url


@pytest.fixture
def base_url():
    from data.constants import BASE_URL
    return BASE_URL


@pytest.fixture
def create_and_delete_courier():
    courier_data = register_new_courier_and_return_login_password()
    login = courier_data[0]
    password = courier_data[1]
    first_name = courier_data[2]
    
    yield login, password, first_name
    
    with allure.step:
        response = requests.post(
            get_login_courier_url(),
            data={"login": login, "password": password}
        )
        if response.status_code == 200:
            courier_id = response.json()["id"]
            delete_response = requests.delete(get_delete_courier_url(courier_id))
            assert delete_response.status_code == 200


@pytest.fixture
def get_courier_id(create_and_delete_courier):
    login, password, _ = create_and_delete_courier
    
    with allure.step:
        response = requests.post(
            get_login_courier_url(),
            data={"login": login, "password": password}
        )
        assert response.status_code == 200
        return response.json()["id"]