# Автор: Разумов Алексей
# Проект автоматизации тестирования API для сервиса "Stellar burgers"


## Установка зависимостей:

`pip install -r requirements.txt`

Запуск тестов:

`pytest -v`

Запуск автотестов и создание отчета о тестировании в Allure:

`pytest --alluredir=allure_results`

Показ отчета из результатов тестов:

`allure serve ./allure_results`

Генерация отчета из результатов тестов:

`allure generate ./allure_results/ -o allure_report `


## Структура проекта

- Diplom2/
  - allure_results/ # отчет с результатами тестирования
  - data/ # тестовые данные
  - helpers/ # вспомогательне генераторы и методы
  - tests/  # автотесты для API сервиса
  - README.md # Текущий файл
  - requirements.txt # Зависимости проекта

  