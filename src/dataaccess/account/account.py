from src.core.db import execute_query
# from src.schema.account import AccountBase
# from src.core.security.security import get_password_hash


def register_account_service(name, email, password):
    res = execute_query("call usp_registration_detail(_name => %s, _gmail => %s,_password => %s)",
                        (name, email, password))
    return res


def login_account_sevice(email, password):
    res = execute_query("call usp_login(_gmail => %s,_password => %s)",
                        (email, password))
    return res