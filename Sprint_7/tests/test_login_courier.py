import pytest
import requests
import allure
from data.constants import REQUIRED_LOGIN_FIELDS, ERROR_MESSAGES
from utils.urls import get_login_courier_url


class TestLoginCourier:
    
    @allure.title
    def test_courier_login_success(self, create_and_delete_courier):
        login, password, _ = create_and_delete_courier
        
        with allure.step:
            response = requests.post(
                get_login_courier_url(),
                data={"login": login, "password": password}
            )
        
        with allure.step:
            assert response.status_code == 200
            response_data = response.json()
            assert "id" in response_data
            assert isinstance(response_data["id"], int)
    
    @allure.title
    @pytest.mark.parametrize("field", REQUIRED_LOGIN_FIELDS)
    def test_login_without_required_field_fails(self, create_and_delete_courier, field):
        login, password, _ = create_and_delete_courier
        
        with allure.step:
            login_data = {"login": login, "password": password}
            del login_data[field]
            
            response = requests.post(get_login_courier_url(), data=login_data)
        
        with allure.step:
            assert response.status_code == 400
            assert response.json()["message"] == ERROR_MESSAGES["login_not_enough_data"]
    
    @allure.title
    def test_login_with_wrong_password_fails(self, create_and_delete_courier):
        login, _, _ = create_and_delete_courier
        
        with allure.step:
            response = requests.post(
                get_login_courier_url(),
                data={"login": login, "password": "wrongpassword"}
            )
        
        with allure.step:
            assert response.status_code == 404
            assert response.json()["message"] == ERROR_MESSAGES["account_not_found"]
    
    @allure.title
    def test_login_with_wrong_login_fails(self, create_and_delete_courier):
        _, password, _ = create_and_delete_courier
        
        with allure.step:
            response = requests.post(
                get_login_courier_url(),
                data={"login": "nonexistentuser", "password": password}
            )
        
        with allure.step:
            assert response.status_code == 404
            assert response.json()["message"] == ERROR_MESSAGES["account_not_found"]
    
    @allure.title
    def test_login_nonexistent_user_fails(self):
        with allure.step:
            response = requests.post(
                get_login_courier_url(),
                data={"login": "nonexistent123", "password": "password123"}
            )
        
        with allure.step:
            assert response.status_code == 404
            assert response.json()["message"] == ERROR_MESSAGES["account_not_found"]