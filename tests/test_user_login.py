import allure
import pytest

from data.user import UserData
from helpers.user import UserHelps


class TestUserLogin:
    @allure.title("Проверка пользователь может авторизоваться по емайл и паролю")
    def test_user_can_login_email_password_success_code_200(self):
        user_api = UserHelps()
        data = user_api.data_random_new_user_account()
        response = user_api.send_request_login(data)
        assert response.status_code == 200
        assert response.json().get("success")

    @pytest.mark.parametrize(
        "test_case, keys",
        [
            pytest.param(
                "Проверка система вернёт ошибку, если неправильно указать email",
                ["email"],
                id="incorrect_email",
            ),
            pytest.param(
                "Проверка система вернёт ошибку, если неправильно указать пароль",
                ["password"],
                id="incorrect_password",
            ),
            pytest.param(
                "Проверка если авторизоваться под несуществующим пользователем, запрос возвращает ошибку",
                ["email", "password"],
                id="incorrect_email_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_user_login_incorrect_shows_error_401(
        self,
        test_case,
        keys,
    ):
        user_api = UserHelps()
        data = user_api.data_random_new_user_account()
        for key in keys:
            data.update(
                {key: f"not_existing_{key}" + user_api.generate_random_string()}
            )
        response = user_api.send_request_login(data)
        assert response.status_code == 401
        assert response.json() == UserData.LOGIN_FIELD_IS_EMPTY

    @pytest.mark.parametrize(
        "test_case, key",
        [
            pytest.param(
                "Проверка если поля email нет, запрос возвращает ошибку",
                "email",
                id="missing_email",
            ),
            pytest.param(
                "Проверка если поля пароль нет, запрос возвращает ошибку",
                "password",
                id="missing_password",
            ),
        ],
    )
    @allure.title("{test_case}")
    def test_user_login_missing_data_shows_error_401(
        self,
        test_case,
        key,
    ):
        user_api = UserHelps()
        data = user_api.data_random_new_user_account()
        data.update({key: ""})
        response = user_api.send_request_login(data)
        assert response.status_code == 401
        assert response.json() == UserData.LOGIN_FIELD_IS_EMPTY
