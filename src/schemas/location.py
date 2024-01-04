from pydantic import BaseModel, validator
from typing import Optional

class Location(BaseModel):
    location_type: str
    order_type: int
    image_data: str
    description: str
    created_by: int
    status: int
    hotel_id: int