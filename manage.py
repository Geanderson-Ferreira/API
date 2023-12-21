from DB_MANAGER.models import create_all
from DB_MANAGER.starter_db_functions import insert_order_with_image, insert_default_values_in_locations, create_hotel_example, create_user_example, insert_default_values_in_order_types, insert_default_values_in_order_status
from sys import argv
import os

def recreate_db():

    IMG = '/home/gean/Documents/Things/app1/DB_MANAGER/DALL·E 2023-07-04 01.04.56 - a dark grey minimalist draw world map.png'

    #Criar as tabelas
    try:
        os.remove('example.db')
    except:
        pass
    create_all()
    create_user_example()
    create_hotel_example()
    insert_default_values_in_order_types()
    insert_default_values_in_order_status()
    insert_default_values_in_locations()
    insert_order_with_image(location_id=1, order_type_id=1, description='Asserehe', created_by_id=1, status_id=1, image_path=None)
    insert_order_with_image(location_id=1, order_type_id=1, description='Hadehe', created_by_id=1, status_id=1, image_path=None)
    insert_order_with_image(location_id=1, order_type_id=1, description='TesteDescricao', created_by_id=1, status_id=1, image_path=None)
    insert_order_with_image(location_id=1, order_type_id=1, description='Culpa da Accor', created_by_id=1, status_id=1, image_path=None)
    insert_order_with_image(location_id=1, order_type_id=1, description='Linus Torvalds', created_by_id=1, status_id=1, image_path=None)

funcoes_argvs = {
    'recreate_db' : recreate_db
}

if argv[1] in funcoes_argvs.keys():
    funcoes_argvs[argv[1]]()