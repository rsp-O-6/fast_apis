from src.core.db import execute_query
from src.schema.IPL import IplAddDetails


def ipl_player_details(fname:str,gmail:str,pwd:str):
    res = execute_query("call usp_test(_fname => %s, _gmail => %s,  _pwd => %s)",
      (fname, gmail, pwd))
    return res