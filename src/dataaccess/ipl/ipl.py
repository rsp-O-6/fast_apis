from src.utilities.utils import execute_query



def ipl_player_details():
    res = execute_query(" call usp_add_player_details()")

    return res