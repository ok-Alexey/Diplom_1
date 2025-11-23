import allure
import requests

from data.user import UserData
from .common import Generators


class UserHelps(Generators): # UserAPIHelper
    @allure.step("Отправка запроса для регистрирования пользователя в системе")
    def send_request_create(self, data):
        return requests.request(
            url=UserData.URL_FOR_CREATE_USER[0],
            method=UserData.URL_FOR_CREATE_USER[1],
            json=data
        )

    @allure.step("Отправка запроса для входа пользователя в систему")
    def send_request_login(
        self,
        user_data
    ):

        url = UserData.USER_URL[0]
        method = UserData.USER_URL[1]

        json_data = {"email": user_data["email"], "password": user_data["password"]}
        return requests.request(url=url, method=method, json=json_data)

    @allure.step("Получение данных нового тестового пользователя")
    def data_random_new_user_account(self, keys=None):
        user_data = self.generate_data_for_create_user(keys=keys)
        response = self.send_request_create(user_data)
        if response.status_code == 200:
            return user_data

    @allure.step("Получение Headers тестового пользователя")
    def get_headers_auth_user(self):
        data = self.data_random_new_user_account()
        response = self.send_request_login(data)
        headers = {"Authorization": response.json().get("accessToken")}
        return headers

    @allure.step("Создание тестовых данных пользователя")
    def generate_data_for_create_user(self, keys=None): # def generate_user_create_data
        name = self.generate_random_string(23)
        password = self.generate_random_string(23)
        email = f"{self.generate_random_string(15)}@{self.generate_random_string(15)}notexists.com"

        full_data = {"name": name, "password": password, "email": email}

        if keys is None:
            return full_data

        return {k: full_data[k] for k in keys if k in full_data}
