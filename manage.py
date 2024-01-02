from DB_MANAGER.models import recreate_db
from DB_MANAGER.populater import populate
from sys import argv
from tests.tester import test_list_orders

# Key é o parametro, o Value é a funcao.
ARGV_FUNCTIONS = {
    'Parametros aceitos no modulo manage.py \n': '',
    'help': lambda: [print('> ', key) for key in ARGV_FUNCTIONS.keys()],
    'recreateDB' : recreate_db,
    'populateDB': populate,
    'list-orders': test_list_orders
}

def run_arguments():
    if len(argv) > 1:
        arg2 = argv[2] if len(argv) > 2 else None

        for i in argv:
            if i in ARGV_FUNCTIONS.keys():
                ARGV_FUNCTIONS[argv[1]]()#(arg2)
                exit()

        print(f"\nFuncao '{argv[1]}' nao definida no escopo manager.\n")

run_arguments()
