from web3 import Web3
from web3 import Account
from web3.exceptions import TransactionNotFound, Web3RPCError

from data.config import arb_rpc, GAS_ZIP_ABI
from models import Parameters, Arbitrum
from utils import read_json, get_next_proxy, get_next_private_key
from colorama import Fore
import time


class GASZip:
    def __init__(self, proxy, private_key):
        self.proxy = proxy
        self.private_key = private_key

        time.sleep(2)

        self.wb3 = Web3(Web3.HTTPProvider(
            endpoint_uri=arb_rpc,
            request_kwargs={'proxies': {'http': self.proxy, 'https': self.proxy}}
        ))

        self._check_connection()

        self.owner_wallet_address = Web3.to_checksum_address(
            self.wb3.eth.account.from_key(self.private_key).address
        )

        self.router_abi = read_json(GAS_ZIP_ABI)
        self.contract = self.wb3.eth.contract(address=self.owner_wallet_address, abi=self.router_abi)

        self.gas_zip_contract_gas_zip_router = '0x26DA582889f59EaaE9dA1f063bE0140CD93E6a4f'


    def _check_connection(self):
        """Проверяет соединение с RPC."""
        try:
            if self.wb3.is_connected():
                print(f'{self.wb3.is_connected()}: RPC работает через прокси {self.proxy}')
            else:
                print(f'{self.wb3.is_connected()}: RPC не работает с прокси {self.proxy}')
        except Exception as e:
            print(Fore.RED + "Ошибка подключения:", e)
        print(self.proxy)


    def get_balance(self):
        """Возвращает баланс в ETH."""
        balance_wei = self.wb3.eth.get_balance(self.owner_wallet_address)
        return Web3.from_wei(balance_wei, 'ether')


    def prepare_transaction_and_sing_and_send(self):
        """Подготавливает транзакцию."""
        params = Parameters()
        parameter = params.get_random_parameter()
        gas_value = params.get_gas_range(str(parameter))

        input_data = self.contract.encode_abi("sendDeposits", [parameter, self.owner_wallet_address])

        checker_gas = self.wb3.eth.get_block('latest')
        base_fee_per_gas = checker_gas['baseFeePerGas'] * 1.01
        max_fee_per_gas = base_fee_per_gas * 1.3
        max_priority_fee_per_gas = base_fee_per_gas / 2

        print(checker_gas)

        tx_wei_value = self.wb3.to_wei(gas_value, 'ether')
        tx = {
            "chainId": Arbitrum.chain_id,
            "from": self.owner_wallet_address,
            "to": self.gas_zip_contract_gas_zip_router,
            "value": tx_wei_value,
            "data": input_data,
            "gas": int(base_fee_per_gas),
            "maxFeePerGas": int(max_fee_per_gas),
            "maxPriorityFeePerGas": int(max_priority_fee_per_gas),
            "nonce": self.wb3.eth.get_transaction_count(self.owner_wallet_address),
        }

        print(tx["nonce"])

        balance_wei = self.wb3.eth.get_balance(self.owner_wallet_address)

        if balance_wei > tx_wei_value:
            try:
                signed_tx = self.wb3.eth.account.sign_transaction(tx, self.private_key)
                time.sleep(2)
                tx_hash = self.wb3.eth.send_raw_transaction(signed_tx.raw_transaction)
                print(f"Transaction hash: {tx_hash.hex()} transaction is successful")
            except Web3RPCError as rpc_error:
                print(Fore.RED + "RPC error:", rpc_error)
            except TransactionNotFound:
                print(Fore.RED + "Transaction not found after sending.")
            except ValueError as value_error:
                print(Fore.RED + "Ошибка в параметрах транзакции:", value_error)
            except Exception as e:
                print(Fore.RED + "Failed to send transaction:", e)
        else:
            print(Fore.RED + f"Insufficient balance: {Web3.from_wei(balance_wei, 'ether')} ETH, required: {Web3.from_wei(tx_wei_value, 'ether')} ETH")