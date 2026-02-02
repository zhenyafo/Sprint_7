import pytest
import requests


class TestCreateOrder:
    
    @pytest.mark.parametrize("color", ["BLACK", "GREY", None, ["BLACK", "GREY"]])
    def test_create_order_with_different_colors(self, base_url, color):
        order_data = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "ул. Ленина, д. 1",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Тестовый заказ"
        }
        
        if color:
            order_data["color"] = color if isinstance(color, list) else [color]
        
        response = requests.post(f"{base_url}/api/v1/orders", json=order_data)
        
        assert response.status_code == 201
        response_data = response.json()
        assert "track" in response_data
        assert isinstance(response_data["track"], int)
    
    def test_create_order_with_black_color(self, base_url):
        response = requests.post(
            f"{base_url}/api/v1/orders",
            json={
                "firstName": "Иван",
                "lastName": "Петров",
                "address": "ул. Ленина, д. 1",
                "metroStation": 4,
                "phone": "+79999999999",
                "rentTime": 5,
                "deliveryDate": "2024-12-31",
                "comment": "Тестовый заказ",
                "color": ["BLACK"]
            }
        )
        
        assert response.status_code == 201
        assert "track" in response.json()
    
    def test_create_order_with_grey_color(self, base_url):
        response = requests.post(
            f"{base_url}/api/v1/orders",
            json={
                "firstName": "Иван",
                "lastName": "Петров",
                "address": "ул. Ленина, д. 1",
                "metroStation": 4,
                "phone": "+79999999999",
                "rentTime": 5,
                "deliveryDate": "2024-12-31",
                "comment": "Тестовый заказ",
                "color": ["GREY"]
            }
        )
        
        assert response.status_code == 201
        assert "track" in response.json()
    
    def test_create_order_with_both_colors(self, base_url):
        response = requests.post(
            f"{base_url}/api/v1/orders",
            json={
                "firstName": "Иван",
                "lastName": "Петров",
                "address": "ул. Ленина, д. 1",
                "metroStation": 4,
                "phone": "+79999999999",
                "rentTime": 5,
                "deliveryDate": "2024-12-31",
                "comment": "Тестовый заказ",
                "color": ["BLACK", "GREY"]
            }
        )
        
        assert response.status_code == 201
        assert "track" in response.json()
    
    def test_create_order_without_color(self, base_url):
        response = requests.post(
            f"{base_url}/api/v1/orders",
            json={
                "firstName": "Иван",
                "lastName": "Петров",
                "address": "ул. Ленина, д. 1",
                "metroStation": 4,
                "phone": "+79999999999",
                "rentTime": 5,
                "deliveryDate": "2024-12-31",
                "comment": "Тестовый заказ"
            }
        )
        
        assert response.status_code == 201
        assert "track" in response.json() 