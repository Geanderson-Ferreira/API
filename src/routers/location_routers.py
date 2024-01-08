from fastapi import APIRouter, Depends, status
from src.schemas.location import LocationSchema
from sqlalchemy.orm import Session
from src.db_manager.depends import get_db_session
from src.db_manager.methods.location_methods import LocationMethods
from fastapi.responses import JSONResponse
from src.db_manager.config import API_PREFIX
from src.db_manager.depends import token_verifier

router = APIRouter(prefix=API_PREFIX + '/location', dependencies=[Depends(token_verifier)])

@router.post('/insert-location/')
def insert_location(location: LocationSchema, db_session: Session = Depends(get_db_session)):

    LocationMethods(db_session).insert_location(location)

    return JSONResponse(
        content={'msg':'success'},
        status_code=status.HTTP_201_CREATED
    )