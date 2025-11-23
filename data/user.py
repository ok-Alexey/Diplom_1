from data.common import MainUrls


class UserData: # UserData
    URL_FOR_CREATE_USER = (f"{MainUrls.URL_STELLARBURGERS_API}/auth/register", "POST") # USER_CREATE_URL

    USER_IS_ALREADY_REGISTERED = { # USER_CREATE_ALREADY_EXISTS_ERROR_403
        "success": False,
        "message": "User already exists",
    }
    REQUIRED_FIELD_IS_NOT_FILLED_IN = { # USER_CREATE_MISSING_FIELD_ERROR_403
        "success": False,
        "message": "Email, password and name are required fields",
    }
    USER_URL = (f"{MainUrls.URL_STELLARBURGERS_API}/auth/login", "POST") # USER_LOGIN_URL
    LOGIN_FIELD_IS_EMPTY = { # USER_LOGIN_MISSING_FIELD_ERROR_401
        "success": False,
        "message": "email or password are incorrect",
    }
