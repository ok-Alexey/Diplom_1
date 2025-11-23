import allure
import pytest

from data.user import UserData
from helpers.user import UserHelps


class TestUserCreate:
    @allure.title("Успешное создание уникального пользователя")
    def test_user_create_account_shows_ok_true_200(self):
        user_api = UserHelps()
        data = user_api.generate_data_for_create_user(keys=["name", "email", "password"])
        response = user_api.send_request_create(data)
        assert response.status_code == 200
        assert response.json().get("success")

    @allure.title("Создать пользователя, который уже зарегистрирован нельзя")
    def test_user_create_account_shows_ok_false_403(self):
        user_api = UserHelps()
        data = user_api.generate_data_for_create_user(keys=["name", "email", "password"])
        user_api.send_request_create(data)
        with allure.step("В данных для регистрации используем другой пароль"):
            data.update(
                {
                    "password": "password" + user_api.generate_random_string(23),
                }
            )
            response = user_api.send_request_create(data)

            assert response.status_code == 403
            assert response.json() == UserData.USER_IS_ALREADY_REGISTERED

    @pytest.mark.parametrize(
        "test_case, fields", 
        [
            pytest.param(
                "Ошибка при незаполненном поле email",
                ["name", "password"],
                id = "email - None",
            ),
            pytest.param(
                "Ошибка при незаполненном поле password",
                ["email", "name"],
                id = "password - None",
            ),
            pytest.param(
                "Ошибка при незаполненном поле name",
                ["email", "password"],
                id = "name - None"
            ),
        ]
    )
    @allure.title("Обязательность заполнения поля {test_case}")
    def test_user_create_account_missing_fields_shows_error_403(self, test_case, fields):
        user_api = UserHelps()

        data = user_api.generate_data_for_create_user(keys=fields)
        response = user_api.send_request_create(data)

        assert response.status_code == 403
        assert response.json() == UserData.REQUIRED_FIELD_IS_NOT_FILLED_IN
