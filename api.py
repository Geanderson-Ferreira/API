from fastapi import FastAPI, Query
from typing import Optional
from DB_MANAGER.methods import queryOrders, queryLocations, queryOrdersSummarized

#Para rodar a API, esteja no mesmo diretorio desde arquivo e rodar:
#>> uvicorn api:app
#>> uvicorn api:app --host 10.0.0.102 --port 8000 --reload

app = FastAPI()


@app.get('/api/list-orders/')
def list_orders(
    IdOrder: Optional[int] = Query(None, alias="IdOrder"),
    Location: Optional[int] = Query(None, alias="Location"),
    CreationDate: Optional[str] = Query(None, alias="CreationDate"),
    EndDate: Optional[str] = Query(None, alias="EndDate"),
    OrderType: Optional[int] = Query(None, alias="OrderType"),
    CreatedBy: Optional[int] = Query(None, alias="CreatedBy"),
    Status: Optional[str] = Query(None, alias="Status")
    ):
    
    return queryOrders(id=IdOrder, 
                       location=Location, 
                       creation_date=CreationDate,
                       end_date=EndDate,
                       order_type=OrderType,
                       created_by=CreatedBy,
                       status=Status)

@app.get('/api/orders_types_summarizeds/')
def orders_types_summarizeds():
    return queryOrdersSummarized()


@app.get('/api/list-locations/')
def list_locations(HotelId: Optional[int] = Query(None, alias='hotel'),
                   LocationType: Optional[str] = Query(None, alias='LocationType'),
                   Floor: Optional[int] = Query(None, alias='floor'),
                   LocationId:Optional[int] = Query(None, alias='LocationId'),
                   ):

    # !Fazer o check se o usuario tem acesso ao hotel todo

    return queryLocations(location_type=LocationType, floor=Floor, hotel_id=HotelId, location_id=LocationId)
