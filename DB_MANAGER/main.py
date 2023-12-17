from models import create_all
from db_methods import create_user_example, insert_default_values_in_order_types
from sys import argv
import os


def recreate_db():
    #Criar as tabelas
    os.remove('example.db')
    create_all()
    create_user_example()
    insert_default_values_in_order_types()


funcoes_argvs = {
    'recreate_db' : recreate_db
}


funcoes_argvs[argv[1]]()