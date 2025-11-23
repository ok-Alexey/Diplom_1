from data.common import MainUrls


class InfoAboutOrder: # OrderData
    URL_FOR_CREATE_ORDER = (f"{MainUrls.URL_STELLARBURGERS_API}/orders", "POST") # ORDER_CREATE_URL
    NO_INGREDIENTS_ARE_INCLUDED_IN_THE_ORDER = { #  ORDER_CREATE_NO_INGREDIENT_ERROR_400
        "success": False,
        "message": "Ingredient ids must be provided",
    }
