from db_methods import create_hotel_example, create_user_example, insert_default_values_in_order_types, insert_default_values_in_order_status
from models import create_all

from sys import argv
import os


def recreate_db():
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


funcoes_argvs = {
    'recreate_db' : recreate_db
}

if argv[1] in funcoes_argvs.keys():
    funcoes_argvs[argv[1]]()