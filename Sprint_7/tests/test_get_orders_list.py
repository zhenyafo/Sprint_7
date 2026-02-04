import pytest
import requests
import allure
from utils.urls import get_orders_url


class TestGetOrdersList:
    
    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_list_returns_list(self):
        with allure.step("Запрос списка заказов"):
            response = requests.get(get_orders_url())
        
        with allure.step("Проверка ответа"):
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
    
    @allure.title("Получение списка заказов с лимитом")
    def test_get_orders_with_limit(self):
        with allure.step("Запрос списка заказов с лимитом 5"):
            response = requests.get(get_orders_url() + "?limit=5")
        
        with allure.step("Проверка лимита"):
            assert response.status_code == 200
            response_data = response.json()
            assert len(response_data["orders"]) <= 5
    
    @allure.title("Получение списка заказов с указанием страницы")
    def test_get_orders_with_page(self):
        with allure.step("Запрос списка заказов с страницы 0"):
            response = requests.get(get_orders_url() + "?page=0")
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            response_data = response.json()
            assert "orders" in response_data
    
    @allure.title("Проверка структуры ответа при получении списка заказов")
    def test_get_orders_list_response_structure(self):
        with allure.step("Запрос списка заказов с лимитом 1"):
            response = requests.get(get_orders_url() + "?limit=1")
        
        with allure.step("Проверка структуры ответа"):
            assert response.status_code == 200
            response_data = response.json()
            
            assert "pageInfo" in response_data
            assert "orders" in response_data
            
            page_info = response_data["pageInfo"]
            assert "page" in page_info
            assert "total" in page_info
            assert "limit" in page_info