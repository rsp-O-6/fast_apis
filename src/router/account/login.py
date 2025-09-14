from fastapi import APIRouter, Depends
from src.schema.account import LoginBase
from src.dataaccess.account import account as data_access
from src.core.security.security import create_access_token
from fastapi import Depends
from src.core.security.security import get_current_user


router = APIRouter()


@router.post("/login")
async def login(req: LoginBase):
    dataset = data_access.login_account_sevice(req.email, req.password)

    if len(dataset) > 0 and len(dataset['rs']): 
        ds = dataset['rs']
        if ds.iloc[0].loc["success"]:
            access_token = create_access_token({"sub": req.email})
            return {
                'success': True,
                'message': ds.iloc[0].loc["message"],
                'access_token': access_token,
                'token_type': 'bearer'
            }
    
        return {'success': False, 'message': ds.iloc[0].loc["message"]}
    
    return {'success': False, 'message': "DATABASE_CONNECTION_ERROR"}





@router.get("/profile")
async def get_profile(current_user: str = Depends(get_current_user)):
    return {"email": current_user, "message": "This is your profile"}