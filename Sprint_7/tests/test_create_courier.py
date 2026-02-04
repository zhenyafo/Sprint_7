import pytest
import requests
import allure
from data.constants import REQUIRED_COURIER_FIELDS, ERROR_MESSAGES
from utils.urls import get_create_courier_url, get_login_courier_url, get_delete_courier_url
from utils.helpers import generate_random_string


class TestCreateCourier:
    
    @allure.title("Нельзя создать курьера без обязательного поля")
    @pytest.mark.parametrize("field", REQUIRED_COURIER_FIELDS)
    def test_create_courier_without_required_field_fails(self, base_url, field):
        with allure.step(f"Создание курьера без поля: {field}"):
            courier_data = {
                "login": "testuser123",
                "password": "password123",
                "firstName": "TestUser"
            }
            
            del courier_data[field]
            
            response = requests.post(get_create_courier_url(), data=courier_data)
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 400
            assert response.json()["message"] == ERROR_MESSAGES["not_enough_data"]
    
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, create_and_delete_courier):
        login, password, first_name = create_and_delete_courier
        
        with allure.step(f"Попытка создания дубликата курьера с логином: {login}"):
            duplicate_courier = {
                "login": login,
                "password": password,
                "firstName": first_name
            }
            
            response = requests.post(get_create_courier_url(), data=duplicate_courier)
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 409
            assert response.json()["message"] == ERROR_MESSAGES["login_already_used"]
    
    @allure.title("Курьера можно создать успешно")
    def test_create_courier_success(self):
        courier_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        with allure.step(f"Создание курьера с логином: {courier_data['login']}"):
            response = requests.post(get_create_courier_url(), data=courier_data)
        
        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 201
            response_data = response.json()
            assert "ok" in response_data
            assert response_data["ok"] is True
        
        with allure.step("Очистка: удаление созданного курьера"):
            login_response = requests.post(
                get_login_courier_url(),
                data={"login": courier_data["login"], "password": courier_data["password"]}
            )
            
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                delete_response = requests.delete(get_delete_courier_url(courier_id))
                assert delete_response.status_code == 200
    
    @allure.title("Проверка структуры ответа при создании курьера")
    def test_create_courier_response_structure(self):
        courier_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        with allure.step(f"Создание курьера для проверки структуры ответа"):
            response = requests.post(get_create_courier_url(), data=courier_data)
        
        with allure.step("Проверка структуры ответа"):
            assert response.status_code == 201
            response_data = response.json()
            assert "ok" in response_data
            assert response_data["ok"] is True
        
        with allure.step("Очистка данных"):
            login_response = requests.post(
                get_login_courier_url(),
                data={"login": courier_data["login"], "password": courier_data["password"]}
            )
            
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                requests.delete(get_delete_courier_url(courier_id))