# sender_stand_request.py
import requests
from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH

def create_order(body):
    """
    Создание заказа.
    :param body: Тело запроса для создания заказа.
    :return: Ответ от API.
    """
    url = BASE_URL + CREATE_ORDER_PATH
    response = requests.post(url, json=body)
    return response

def get_order_by_track(track_number):
    """
    Получение заказа по треку.
    :param track_number: Номер трека заказа.
    :return: Ответ от API.
    """
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH
    params = {'t': track_number}
    response = requests.get(url, params=params)
    return response
