from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

class TestBurger:
    def test_burger_after_created_has_not_ingredients(self): # После создания бургер не имеет ингредиентов
        burger = Burger()
        assert burger.ingredients == []

    def test_burger_after_created_has_not_buns(self): # После создания бургер не имеет булочек
        burger = Burger()
        assert burger.bun is None


    def test_add_ingredient_quantity_is_equal_to_the_set_value(self): # Количество ингредиентов бургера соответствует количеству установленных ингредиентов при его создании
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "ingredient_for_test"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1


    def test_set_buns(self): # Название булочки соответствует назначенной при создании бургера
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "bun_for_test"
        mock_bun.get_price.return_value = 500.0

        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient_obj_match(self): # Название ингредиента соответствует назначенному при создании бургера
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "ingredient_for_test"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_after_removing_number_of_burger_ingredients_is_equal_to_zero(self): # После удаления добавленного ингредиента количество ингредиентов бургера равно нулю
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "ingredient_for_test"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_moving_ingredients_to_different_positions(self): # Проверка перемещения ингредиентов на разные позиции
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_1.get_name.return_value = "ingredient_for_test_1"

        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_2.get_name.return_value = "ingredient_for_test_2"

        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self): # Расчёт цены бургера с добавленными ингредиентами
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "bun_for_test"
        mock_bun.get_price.return_value = 500.0

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "ingredient_for_test"
        mock_ingredient.get_price.return_value = 400.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert (burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price())


    def test_get_receipt(self): # Получение чека с информацией о бургере
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "bun_for_test"
        mock_bun.get_price.return_value = 500.0

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "ingredient_for_test"
        mock_ingredient.get_price.return_value = 400.0
        mock_ingredient.get_type.return_value = "sauce"

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert receipt == (
            "(==== bun_for_test ====)\n"
            "= sauce ingredient_for_test =\n"
            "(==== bun_for_test ====)\n\n"
            "Price: 1400.0"
        )
