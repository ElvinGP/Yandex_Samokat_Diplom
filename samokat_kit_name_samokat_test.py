# samokat_kit_name_samokat_test.py
import sender_stand_request

def test_create_and_get_order():
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.create_order()
    assert create_response.status_code == 201, f"Ожидался код 201, получен {create_response.status_code}"
    
    # Шаг 2: Сохранение номера трека заказа
    track_number = create_response.json().get('track')
    assert track_number is not None, "Номер трека не был возвращен в ответе"
    
    # Шаг 3: Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"
    
    # Шаг 4: Проверка данных заказа
    order_info = get_response.json().get('order')
    assert order_info is not None, "Информация о заказе не была возвращена"
    assert order_info['firstName'] == "Naruto", "Имя заказчика не совпадает"