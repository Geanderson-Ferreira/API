from pydantic import BaseModel, validator
from typing import Optional

class OrderSchema(BaseModel):
    location: int
    order_type: int
    image_data: str
    description: str
    created_by: int
    status: int
    hotel_id: int
    
class FilterOrderSchema(BaseModel):
    id: Optional[int] = None
    location: Optional[int] = None
    order_type: Optional[int] = None
    image_data: Optional[str] = None
    description: Optional[str] = None
    created_by: Optional[int] = None
    status: Optional[int] = None
    hotel_id: Optional[int] = None
    
    @validator("id", "location", "order_type", "image_data", "description", "created_by", "status", "hotel_id", pre=True, always=True)
    def convert_optional_fields_to_none(cls, value):
        return None if not value else value
        #return value if value is not None and value != "" else None
