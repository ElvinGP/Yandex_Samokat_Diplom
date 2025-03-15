# sender_stand_request.py
import requests
from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import order_data

def create_order():
    url = BASE_URL + CREATE_ORDER_PATH
    response = requests.post(url, json=order_data)
    return response

def get_order_by_track(track_number):
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH
    params = {'t': track_number}
    response = requests.get(url, params=params)
    return response