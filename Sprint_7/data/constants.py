BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_ENDPOINT = "/api/v1/courier"
LOGIN_COURIER_ENDPOINT = "/api/v1/courier/login"
ORDERS_ENDPOINT = "/api/v1/orders"
DELETE_COURIER_ENDPOINT = "/api/v1/courier/{id}"

ORDER_DATA = {
    "firstName": "Иван",
    "lastName": "Петров",
    "address": "ул. Ленина, д. 1",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 5,
    "deliveryDate": "2024-12-31",
    "comment": "Тестовый заказ"
}
BLACK_COLOR = "BLACK"
GREY_COLOR = "GREY"

ERROR_MESSAGES = {
    "not_enough_data": "Недостаточно данных для создания учетной записи",
    "login_already_used": "Этот логин уже используется. Попробуйте другой.",
    "login_not_enough_data": "Недостаточно данных для входа",
    "account_not_found": "Учетная запись не найдена"
}

REQUIRED_COURIER_FIELDS = ["login", "password", "firstName"]

REQUIRED_LOGIN_FIELDS = ["login", "password"] 