import pytest
import requests
import allure
from data.constants import ORDER_DATA, BLACK_COLOR, GREY_COLOR
from utils.urls import get_orders_url
from utils.helpers import create_test_order


class TestCreateOrder:
    
    @allure.title
    @pytest.mark.parametrize("color", [BLACK_COLOR, GREY_COLOR, None, [BLACK_COLOR, GREY_COLOR]])
    def test_create_order_with_different_colors(self, color):
        order_data = ORDER_DATA.copy()
        
        if color:
            order_data["color"] = color if isinstance(color, list) else [color]
        
        with allure.step:
            response = requests.post(get_orders_url(), json=order_data)
        
        with allure.step:
            assert response.status_code == 201
            response_data = response.json()
            assert "track" in response_data
            assert isinstance(response_data["track"], int)
    
    @allure.title
    def test_create_order_with_black_color(self):
        with allure.step:
            response = create_test_order(BLACK_COLOR)
        
        with allure.step:
            assert response.status_code == 201
            assert "track" in response.json()
    
    @allure.title
    def test_create_order_with_grey_color(self):
        with allure.step:
            response = create_test_order(GREY_COLOR)
        
        with allure.step:
            assert response.status_code == 201
            assert "track" in response.json()
    
    @allure.title
    def test_create_order_with_both_colors(self):
        with allure.step:
            response = create_test_order([BLACK_COLOR, GREY_COLOR])
        
        with allure.step:
            assert response.status_code == 201
            assert "track" in response.json()
    
    @allure.title
    def test_create_order_without_color(self):
        with allure.step:
            response = create_test_order()
        
        with allure.step:
            assert response.status_code == 201
            assert "track" in response.json()