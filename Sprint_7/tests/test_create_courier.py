import pytest
import requests


class TestCreateCourier:
    
    @pytest.mark.parametrize("field", ["login", "password", "firstName"])
    def test_create_courier_without_required_field_fails(self, base_url, field):
        courier_data = {
            "login": "testuser123",
            "password": "password123",
            "firstName": "TestUser"
        }
        
        del courier_data[field]
        
        response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
    
    def test_create_duplicate_courier_fails(self, base_url, create_and_delete_courier):
        login, password, first_name = create_and_delete_courier
        
        duplicate_courier = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        
        response = requests.post(f"{base_url}/api/v1/courier", data=duplicate_courier)
        
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."
    
    def test_create_courier_success(self, base_url):
        from utils.helpers import generate_random_string
        
        courier_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
        
        assert response.status_code == 201
        assert response.json()["ok"] is True
        
        login_response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": courier_data["login"], "password": courier_data["password"]}
        )
        
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f"{base_url}/api/v1/courier/{courier_id}")
    
    def test_create_courier_response_structure(self, base_url):
        from utils.helpers import generate_random_string
        
        courier_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        
        response = requests.post(f"{base_url}/api/v1/courier", data=courier_data)
        
        assert response.status_code == 201
        response_data = response.json()
        assert "ok" in response_data
        assert response_data["ok"] is True
        
        login_response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": courier_data["login"], "password": courier_data["password"]}
        )
        
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f"{base_url}/api/v1/courier/{courier_id}") 