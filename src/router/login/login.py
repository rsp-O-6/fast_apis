from fastapi import APIRouter, Depends
from src.schema.IPL import IplAddDetails
from src.dataaccess.ipl import ipl as ipl_data_access

router = APIRouter()

@router.post('/ipl_player_details')
def ipl_player_details(req:IplAddDetails):

    try:
        return {"success":"true"}
        



    except Exception as error:
        print(error)



