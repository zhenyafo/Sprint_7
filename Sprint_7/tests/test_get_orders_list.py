import pytest
import requests


class TestGetOrdersList:
    
    def test_get_orders_list_returns_list(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders")
        
        assert response.status_code == 200
        response_data = response.json()
        
        assert "orders" in response_data
        assert isinstance(response_data["orders"], list)
        
        if response_data["orders"]:
            first_order = response_data["orders"][0]
            assert "id" in first_order
            assert "firstName" in first_order
            assert "lastName" in first_order
            assert "address" in first_order
            assert "metroStation" in first_order
            assert "phone" in first_order
            assert "rentTime" in first_order
            assert "deliveryDate" in first_order
            assert "track" in first_order
            assert "color" in first_order
            assert "comment" in first_order
            assert "cancelled" in first_order
            assert "finished" in first_order
            assert "inDelivery" in first_order
            assert "courierFirstName" in first_order
            assert "createdAt" in first_order
            assert "updatedAt" in first_order
            assert "status" in first_order
    
    def test_get_orders_with_limit(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders?limit=5")
        
        assert response.status_code == 200
        response_data = response.json()
        assert len(response_data["orders"]) <= 5
    
    def test_get_orders_with_page(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders?page=0")
        
        assert response.status_code == 200
        response_data = response.json()
        assert "orders" in response_data
    
    def test_get_orders_list_response_structure(self, base_url):
        response = requests.get(f"{base_url}/api/v1/orders?limit=1")
        
        assert response.status_code == 200
        response_data = response.json()
        
        assert "pageInfo" in response_data
        assert "orders" in response_data
        
        page_info = response_data["pageInfo"]
        assert "page" in page_info
        assert "total" in page_info
        assert "limit" in page_info 