import pytest
import requests
import allure
from utils.urls import get_orders_url


class TestGetOrdersList:
    
    @allure.title
    def test_get_orders_list_returns_list(self):
        with allure.step:
            response = requests.get(get_orders_url())
        
        with allure.step:
            assert response.status_code == 200
            response_data = response.json()
            
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)
            
            if response_data["orders"]:
                first_order = response_data["orders"][0]
                required_fields = [
                    "id", "firstName", "lastName", "address", "metroStation",
                    "phone", "rentTime", "deliveryDate", "track", "color",
                    "comment", "cancelled", "finished", "inDelivery",
                    "courierFirstName", "createdAt", "updatedAt", "status"
                ]
                
                for field in required_fields:
                    assert field in first_order, f"Поле {field} отсутствует в ответе"
    
    @allure.title
    def test_get_orders_with_limit(self):
        with allure.step:
            response = requests.get(get_orders_url() + "?limit=5")
        
        with allure.step:
            assert response.status_code == 200
            response_data = response.json()
            assert len(response_data["orders"]) <= 5
    
    @allure.title
    def test_get_orders_with_page(self):
        with allure.step:
            response = requests.get(get_orders_url() + "?page=0")
        
        with allure.step:
            assert response.status_code == 200
            response_data = response.json()
            assert "orders" in response_data
    
    @allure.title
    def test_get_orders_list_response_structure(self):
        with allure.step:
            response = requests.get(get_orders_url() + "?limit=1")
        
        with allure.step:
            assert response.status_code == 200
            response_data = response.json()
            
            assert "pageInfo" in response_data
            assert "orders" in response_data
            
            page_info = response_data["pageInfo"]
            assert "page" in page_info
            assert "total" in page_info
            assert "limit" in page_info