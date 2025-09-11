from fastapi import APIRouter, Depends
from src.schema.IPL import IplAddDetails
from src.dataaccess.ipl  import   ipl as data_access

router = APIRouter()

@router.post('/ipl_player_details')
def ipl_player_details(req:IplAddDetails):

    try:

        data_access.ipl_player_details(fname=req.name,gmail=req.gmail,pwd=req.pasword)
        return {True:"success"}
        


    except Exception as error:
        print(error)



