import random

import allure
import requests

from data.ingredients import InfoAboutIngredients
from data.order import InfoAboutOrder
from .common import Generators


class OrderHelps(Generators): # OrderAPIHelper(Generators)
    @allure.step("Отправка запроса для создания заказа в системе")
    def send_request_create(self, data, headers=None):
        return requests.request(
            url=InfoAboutOrder.URL_FOR_CREATE_ORDER[0],
            method=InfoAboutOrder.URL_FOR_CREATE_ORDER[1],
            json=data,
            headers=headers
        )

    @allure.step("Отправка запроса для получения списка ингредиентов из системы")
    def send_request_get_ingredients(self):
        response = requests.request(
            url=InfoAboutIngredients.URL_FOR_GET_INGREDIENTS_LIST[0],
            method=InfoAboutIngredients.URL_FOR_GET_INGREDIENTS_LIST[1]
        )
        if response.status_code == 200:
            response_json = response.json()
            data = response_json["data"]
            output = []
            for ingredient in data:
                output.append(ingredient["_id"])
            return output

    @allure.step("Создание тестовых данных заказа")
    def generate_order_create_data(self):
        ingredients = self.send_request_get_ingredients()
        return {"ingredients": random.sample(ingredients, 2)}
