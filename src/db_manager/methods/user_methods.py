from sqlalchemy.orm import Session
from src.db_manager.models import User
from src.schemas.user import UserSchema, UserSchemaForLogin
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi import status
from datetime import datetime, timedelta
from src.db_manager.config import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

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
    
    def user_login(self, user: UserSchemaForLogin, expires_in: int = 30):
        user_on_db = self.db_session.query(User).filter_by(Username=user.username).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username or Password Invalid."
            )
        
        if not crypt_context.verify(user.password, user_on_db.Password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username or Password Invalid."
            )
        
        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub' : user.username,
            'exp' : exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

        return {'access_token' : access_token,
                'exp' : exp.isoformat()
                }
