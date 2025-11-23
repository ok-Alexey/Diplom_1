import random
import string

import allure


class Generators: # CommonApiHelper
    @allure.step("Создание случайных значений {length} шт.")
    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
