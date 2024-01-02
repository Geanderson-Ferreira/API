from pydantic import BaseModel

class OrderSchema(BaseModel):
    location: int
    order_type: int
    image_data: str
    description: str
    created_by: int
    status: int
    hotel_id: int