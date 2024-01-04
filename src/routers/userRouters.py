from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from src.db_manager.config import API_PREFIX
from sqlalchemy.orm import Session
from src.db_manager.depends import get_db_session
from src.db_manager.methods.user_methods import UserMethod
from src.schemas.user import UserSchema

router  = APIRouter(prefix=API_PREFIX)

@router.post('/register_user')
def user_register(
    user: UserSchema,
    db_session: Session = Depends(get_db_session)
    ):

    u = UserMethod(db_session)
    u.register_user(user=user)
    
    return JSONResponse(
        content={'msg':'success'},
        status_code=status.HTTP_201_CREATED
    )

    