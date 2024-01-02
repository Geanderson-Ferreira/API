from sqlalchemy.orm import Session
from src.db_manager.models import User
from src.schemas.user import UserSchema
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status

crypt_context = CryptContext(schemes=['sha256_crypt'])

class UserMethod:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def register_user(self, user: UserSchema):
        user_to_insert = User(
            Username=user.username,
            Password=crypt_context.hash(user.password),
            FullName=user.fullname,
            Email=user.email
        )
        try:
            self.db_session.add(user_to_insert)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User Data Already Exists'
            )

