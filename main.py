from gas_zip_task import GASZip
from utils import my_time_sleep, get_next_proxy,get_next_private_key
from utils import title_text
from colorama import init, Fore

import time


def main():
    try:
        for _ in range(6): # В скобку вписать число идентичное колличеству приватных ключей в файле 
            gaszip = GASZip(proxy=get_next_proxy(),private_key=get_next_private_key())
            gaszip.prepare_transaction_and_sing_and_send()
            time.sleep(my_time_sleep())

    except KeyboardInterrupt:
        print("Работа завершена пользователем.")
    except Exception as e:
        print(f"Ошибка во время выполнения: {e}")

if __name__=='__main__':
    main()

print(f'Soft is Finished')
init(autoreset=True)
print(Fore.GREEN + title_text)








