from DB_MANAGER.models import recreate_db
from DB_MANAGER.populater import populate
from sys import argv
import os

# Key é o parametro, o Value é a funcao.
ARGV_FUNCTIONS = {
    'Parametros aceitos no modulo manage.py \n': '',
    'help': lambda: [print('> ', key) for key in ARGV_FUNCTIONS.keys()],
    'recreateDB' : recreate_db,
    'populateDB': populate,
    
}


def run_arguments():
    for i in argv:
        if i in ARGV_FUNCTIONS.keys():
            ARGV_FUNCTIONS[argv[1]]()
            exit()
    print('Funcao nao definida no escopo manager.')

run_arguments()
