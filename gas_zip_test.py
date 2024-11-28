# from web3 import Web3
# from eth_account import Account
# from web3.exceptions import TransactionNotFound, Web3RPCError
# from data.config import arb_rpc
# from data.config import GAS_ZIP_ABI
# from utils import read_json, get_next_proxy, get_next_private_key
# from models import Parameters, Network
# from models import Arbitrum
# from client import Client
# from colorama import init, Fore

# import time
# import json
# import random
# import requests



# proxy = get_next_proxy()
# private_key = get_next_private_key()

# web3 = Web3(Web3.HTTPProvider(endpoint_uri=arb_rpc, request_kwargs={'proxies':{'http': proxy,'https': proxy}}))
# try:
#     if web3.is_connected():
#         print(f'{web3.is_connected()}: RPC работает через прокси {proxy}')
#     else:
#         print(f'{web3.is_connected()}: RPC не работает с прокси {proxy}')
# except Exception as e:
#     print("Ошибка подключения:", e)
# print(proxy)

# # get from privat key to address:
# owner_wallet_address = Web3.to_checksum_address(web3.eth.account.from_key(private_key=private_key).address)

# # данные контрактов
# arb_smart_contract = '0x912CE59144191C1204E64559FE8253a0e49E6548'
# gas_zip_contract_gas_zip_router = '0x26DA582889f59EaaE9dA1f063bE0140CD93E6a4f'
# # роутер для ABI
# router_abi = read_json(GAS_ZIP_ABI)

# # создание контракта
# contract = web3.eth.contract(address=owner_wallet_address, abi=router_abi)

# balance_eth_in_arb_wei = web3.eth.get_balance(owner_wallet_address)
# balance_eth_in_arb = Web3.from_wei(balance_eth_in_arb_wei, 'ether')

# params = Parameters()
# parametr = params.get_random_parameter()
# gas_value = params.get_gas_range(str(parametr))

# time.sleep(1)

# input_data = contract.encode_abi("sendDeposits",[parametr, owner_wallet_address]) 

# checker_gas = web3.eth.get_block('latest')
# base_fee_per_gas = checker_gas['baseFeePerGas'] * 1.01
# max_fee_per_gas = base_fee_per_gas * 1.3
# max_priority_fee_per_gas = base_fee_per_gas / 2

# print(checker_gas)

# tx_wei_value = web3.to_wei(gas_value, 'ether')

# tx = {
#     "chainId": Arbitrum.chain_id,
#     "from": owner_wallet_address,
#     "to": gas_zip_contract_gas_zip_router,
#     "value":tx_wei_value,
#     "data": input_data,
#     "gas": int(base_fee_per_gas),
#     "maxFeePerGas": int(max_fee_per_gas),
#     "maxPriorityFeePerGas": int(max_priority_fee_per_gas),
#     "nonce": web3.eth.get_transaction_count(owner_wallet_address),
# }

# print(f'{tx["nonce"]}{owner_wallet_address}')

# signed_tx = web3.eth.account.sign_transaction(tx, private_key)
# print(signed_tx)

# time.sleep(3)

# tx_wei = Web3.from_wei(tx_wei_value, 'ether')

# if balance_eth_in_arb > tx_wei:
#     try:
#         tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
#         print(f"Transaction hash: {tx_hash.hex()} transaction is succesful")
#     except Web3RPCError as rpc_error:
#         print("RPC error:", rpc_error)
#     except TransactionNotFound:
#         print("Transaction not found after sending.")
#     except ValueError as value_error:
#         print("Ошибка в параметрах транзакции:", value_error)
#     except Exception as e:
#         print("Failed to send transaction:", e)

# else:
#     print(f'{ValueError} balance wallet_sender is not enough coins')

# init(autoreset=True)

# title_text = '''
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
# title_text_2 = '''
# //   $$$$$$\                            $$\      $$\  $$$$$$\  $$\   $$\                     $$\   $$\     $$\             $$$$$$$$\ $$$$$$$$\ $$\   $$\ 
# //  $$  __$$\                           $$$\    $$$ |$$  __$$\ $$$\  $$ |                    \__|  $$ |    $$ |            $$  _____|\__$$  __|$$ |  $$ |
# //  $$ /  \__| $$$$$$\   $$$$$$\        $$$$\  $$$$ |$$ /  $$ |$$$$\ $$ |      $$\  $$\  $$\ $$\ $$$$$$\   $$$$$$$\        $$ |         $$ |   $$ |  $$ |
# //  $$$$\     $$  __$$\ $$  __$$\       $$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |      $$ | $$ | $$ |$$ |\_$$  _|  $$  __$$\       $$$$$\       $$ |   $$$$$$$$ |
# //  $$  _|    $$ /  $$ |$$ |  \__|      $$ \$$$  $$ |$$  __$$ |$$ \$$$$ |      $$ | $$ | $$ |$$ |  $$ |    $$ |  $$ |      $$  __|      $$ |   $$  __$$ |
# //  $$ |      $$ |  $$ |$$ |            $$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |      $$ | $$ | $$ |$$ |  $$ |$$\ $$ |  $$ |      $$ |         $$ |   $$ |  $$ |
# //  $$ |      \$$$$$$  |$$ |            $$ | \_/ $$ |$$ |  $$ |$$ | \$$ |      \$$$$$\$$$$  |$$ |  \$$$$  |$$ |  $$ |      $$$$$$$$\    $$ |   $$ |  $$ |
# //  \__|       \______/ \__|            \__|     \__|\__|  \__|\__|  \__|       \_____\____/ \__|   \____/ \__|  \__|      \________|   \__|   \__|  \__|                                                                                                                                                      
# '''

