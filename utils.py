import json
import random
from typing import Union, Optional
from models import Parameters
from itertools import cycle


def read_json(path: str, encoding: Optional[str] = None) -> list | dict: # функция для удобного чтения json ABI 
    return json.load(open(path, encoding=encoding))

def my_time_sleep():
    return random.randint(5, 10) # В скобках указан отрезок в секундах между перекдючением аккаунтов:

def random_gas_fuel_value():
    tmp_value =  random.uniform(2.0384535007747e-05, 4.0384535007747e-05)
    wei_value = int(tmp_value * 10**18)
    return wei_value

def get_parametrs():
    params = Parameters()
    parametr = params.get_random_parameter()
    gas_value = params.get_gas_range(str(parametr))
    return gas_value

def get_next_private_key():
    with open('private_keys.txt', 'r') as file:
        private_keys = [line.strip() for line in file.readlines()]

    try:
        with open('private_key_index.txt', 'r') as index_file:
            index = int(index_file.read().strip())
    except FileNotFoundError:
        index = 0

    private_key = private_keys[index % len(private_keys)]  

    with open('private_key_index.txt', 'w') as index_file:
        index_file.write(str((index + 1) % len(private_keys)))

    return private_key

def get_next_proxy():
    with open('proxy.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    try:
        with open('proxy_index.txt', 'r') as index_file:
            index = int(index_file.read().strip())
    except FileNotFoundError:
        
        index = 0
    proxy = proxies[index % len(proxies)] 

    with open('proxy_index.txt', 'w') as index_file:
        index_file.write(str((index + 1) % len(proxies)))

    return proxy


title_text = '''
# //  $$$$$$$\   $$$$$$\     $$$$$\  $$$$$$\  $$$$$$$\  $$$$$$\ $$\   $$\          $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$$\ 
# //  $$  __$$\ $$  __$$\    \__$$ |$$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |        $$  __$$\ $$  __$$\ $$  _____|\__$$  __|
# //  $$ |  $$ |$$ /  $$ |      $$ |$$ /  $$ |$$ |  $$ |  $$ |  $$$$\ $$ |        $$ /  \__|$$ /  $$ |$$ |         $$ |   
# //  $$$$$$$\ |$$ |  $$ |      $$ |$$$$$$$$ |$$$$$$$  |  $$ |  $$ $$\$$ |        \$$$$$$\  $$ |  $$ |$$$$$\       $$ |   
# //  $$  __$$\ $$ |  $$ |$$\   $$ |$$  __$$ |$$  __$$<   $$ |  $$ \$$$$ |         \____$$\ $$ |  $$ |$$  __|      $$ |   
# //  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |\$$$ |        $$\   $$ |$$ |  $$ |$$ |         $$ |   
# //  $$$$$$$  | $$$$$$  |\$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$\ $$ | \$$ |        \$$$$$$  | $$$$$$  |$$ |         $$ |   
# //  \_______/  \______/  \______/ \__|  \__|\__|  \__|\______|\__|  \__|$$$$$$\  \______/  \______/ \__|         \__|   
# //                                                                      \______|                                        
# '''

