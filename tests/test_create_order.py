import allure

from data.order import InfoAboutOrder
from helpers.order import OrderHelps
from helpers.user import UserHelps


class TestOrderCreate:

    @allure.title("Без авторизации:Проверка создания заказа c ингредиентами")
    def test_no_auth_order_create_success_shows_200(self):
        order_api = OrderHelps()
        data = order_api.generate_order_create_data()
        response = order_api.send_request_create(data)
        assert response.status_code == 200
        assert response.json().get("success")

    @allure.title(
        "Без авторизации: Проверка создания заказа с невалидным хэшем - ошибка 500"
    )
    def test_no_auth_order_create_invalidate_hash_ingredient_error_500(self):
        order_api = OrderHelps()
        data = {"ingredients": ["123Notvalid"]}
        response = order_api.send_request_create(data)
        assert response.status_code == 500

    @allure.title(
        "Без авторизации: Проверка создания заказа без ингредиентов - ошибка 400"
    )
    def test_no_auth_order_create_no_ingredient_error_400(self):
        order_api = OrderHelps()
        data = {"ingredients": []}
        response = order_api.send_request_create(data)
        assert response.status_code == 400
        assert response.json() == InfoAboutOrder.NO_INGREDIENTS_ARE_INCLUDED_IN_THE_ORDER

    @allure.title("C Авторизацией: Проверка создания заказа")
    def test_auth_order_create_success_shows_200(self):

        user_api = UserHelps()
        headers = user_api.get_headers_auth_user()

        order_api = OrderHelps()
        data = order_api.generate_order_create_data()
        response = order_api.send_request_create(data, headers=headers)

        assert response.status_code == 200
        assert response.json().get("success")
