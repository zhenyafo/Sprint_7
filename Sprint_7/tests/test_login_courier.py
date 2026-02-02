import pytest
import requests


class TestLoginCourier:
    
    def test_courier_login_success(self, base_url, create_and_delete_courier):
        login, password, _ = create_and_delete_courier
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": login, "password": password}
        )
        
        assert response.status_code == 200
        response_data = response.json()
        assert "id" in response_data
        assert isinstance(response_data["id"], int)
    
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_without_required_field_fails(self, base_url, field, create_and_delete_courier):
        login, password, _ = create_and_delete_courier
        
        login_data = {"login": login, "password": password}
        del login_data[field]
        
        response = requests.post(f"{base_url}/api/v1/courier/login", data=login_data)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
    
    def test_login_with_wrong_password_fails(self, base_url, create_and_delete_courier):
        login, _, _ = create_and_delete_courier
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": login, "password": "wrongpassword"}
        )
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
    
    def test_login_with_wrong_login_fails(self, base_url, create_and_delete_courier):
        _, password, _ = create_and_delete_courier
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": "nonexistentuser", "password": password}
        )
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
    
    def test_login_nonexistent_user_fails(self, base_url):
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            data={"login": "nonexistent123", "password": "password123"}
        )
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена" 