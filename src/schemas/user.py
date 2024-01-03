import re
from pydantic import BaseModel, validator


class UserSchema(BaseModel):
    username: str
    password: str
    fullname: str
    email: str
    type: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username Format Invalid.')
        return value