# Гаджиев Эльвин 27 кагорта - Финальный проект. Инженер по тестированию плюс. 
# samokat_kit_name_samokat_test.py
import sender_stand_request
from data import order_data_1

def test_create_and_get_order():
    """
    Тест проверяет создание заказа и получение его по треку.
    """
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.create_order(order_data_1)
    assert create_response.status_code == 201, f"Ожидался код 201, получен {create_response.status_code}"
    
    # Шаг 2: Получение заказа по треку
    track_number = create_response.json().get('track')
    get_response = sender_stand_request.get_order_by_track(track_number)
    
    # Шаг 3: Проверка, что заказ найден
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"
    assert get_response.json().get('order') is not None, "Заказ не был найден"
