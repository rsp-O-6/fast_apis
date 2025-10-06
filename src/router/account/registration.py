from fastapi import APIRouter, Depends
from src.schema.account import AccountBase
from src.dataaccess.account import account as data_access


router = APIRouter()


@router.post("/register")
async def register_account(req: AccountBase):

    dataset = data_access.register_account_service(req.name, req.email, req.password)

    if len(dataset)>0 and len(dataset['rs']): 
        ds = dataset['rs']
        if(ds.iloc[0].loc["success"]):
            return {'success': True, 'message': ds.iloc[0].loc["message"] }
    
        return {'success': False, 'message': ds.iloc[0].loc["message"] }
    
    return {'success': False, 'message': "DATABASE_CONNECTION_ERROR"}