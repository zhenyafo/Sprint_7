from data.constants import BASE_URL, CREATE_COURIER_ENDPOINT, LOGIN_COURIER_ENDPOINT, ORDERS_ENDPOINT, DELETE_COURIER_ENDPOINT


def get_create_courier_url():
    return BASE_URL + CREATE_COURIER_ENDPOINT


def get_login_courier_url():
    return BASE_URL + LOGIN_COURIER_ENDPOINT


def get_orders_url():
    return BASE_URL + ORDERS_ENDPOINT


def get_delete_courier_url(courier_id):
    return BASE_URL + DELETE_COURIER_ENDPOINT.format(id=courier_id)


def get_order_by_track_url(track):
    return BASE_URL + ORDERS_ENDPOINT + f"/track?t={track}" 