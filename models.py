from dataclasses import dataclass
from decimal import Decimal
from typing import Union
import random


@dataclass
class DefaultABIs:
    """
    The default ABIs.
    """
    Token = [
        {
            'constant': True,
            'inputs': [],
            'name': 'name',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'symbol',
            'outputs': [{'name': '', 'type': 'string'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'totalSupply',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [],
            'name': 'decimals',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [{'name': 'who', 'type': 'address'}],
            'name': 'balanceOf',
            'outputs': [{'name': '', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': True,
            'inputs': [{'name': '_owner', 'type': 'address'}, {'name': '_spender', 'type': 'address'}],
            'name': 'allowance',
            'outputs': [{'name': 'remaining', 'type': 'uint256'}],
            'payable': False,
            'stateMutability': 'view',
            'type': 'function'
        },
        {
            'constant': False,
            'inputs': [{'name': '_spender', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}],
            'name': 'approve',
            'outputs': [],
            'payable': False,
            'stateMutability': 'nonpayable',
            'type': 'function'
        },
        {
            'constant': False,
            'inputs': [{'name': '_to', 'type': 'address'}, {'name': '_value', 'type': 'uint256'}],
            'name': 'transfer',
            'outputs': [], 'payable': False,
            'stateMutability': 'nonpayable',
            'type': 'function'
        }]


class TokenAmount:
    Wei: int
    Ether: Decimal
    decimals: int

    def __init__(self, amount: Union[int, float, str, Decimal], decimals: int = 18, wei: bool = False) -> None:
        if wei:
            self.Wei: int = amount
            self.Ether: Decimal = Decimal(str(amount)) / 10 ** decimals

        else:
            self.Wei: int = int(Decimal(str(amount)) * 10 ** decimals)
            self.Ether: Decimal = Decimal(str(amount))

        self.decimals = decimals


class Network:
    def __init__(self,
                 name: str,
                 rpc: str,
                 chain_id: int,
                 eip1559_tx: bool,
                 coin_symbol: str,
                 explorer: str,
                 decimals: int = 18,
                 ):
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.eip1559_tx = eip1559_tx
        self.coin_symbol = coin_symbol
        self.decimals = decimals
        self.explorer = explorer

    def __str__(self):
        return f'{self.name}'


Arbitrum = Network(
    name='arbitrum',
    rpc='https://rpc.ankr.com/arbitrum/',
    chain_id=42161,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://arbiscan.io/',
)


Optimism = Network(
    name='optimism',
    rpc='https://rpc.ankr.com/optimism/',
    chain_id=10,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://optimistic.etherscan.io/',
)


Polygon = Network(
    name='polygon',
    rpc='https://polygon-rpc.com/',
    chain_id=137,
    eip1559_tx=True,
    coin_symbol='MATIC',
    explorer='https://polygonscan.com/',
)


Base = Network(
    name='base',
    rpc='https://base.llamarpc.com',
    chain_id=8453,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://basescan.org/',
)


ZkSync = Network(
    name='zksync',
    rpc='https://zksync.meowrpc.com',
    chain_id=324,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://explorer.zksync.io/',
)


Linea = Network(
    name='linea',
    rpc='https://linea.drpc.org',
    chain_id=59144,
    eip1559_tx=True,
    coin_symbol='ETH',
    explorer='https://lineascan.build/',
)


class Parameters:
    def __init__(self):
        self.arbitrum_nowa = [813516390681270555804077180250817355577000832950161774617301439270092800]
        self.base = [813759030201274911562229183386600532253063567249964639769631371762335744] 
        self.bnb = [811548314574568559099066488149464922537825321407316312826180875721900032]
        self.fantom = [811817914041240065497013158300335118844561692851541718550991911824392192]
        self.gnosis = [812707592281256036610237169798206766656791718617485557442868330962616320]
        self.injective_evm = [815107027534632443551962534140951513786745424471091668393686552274796544]
        self.kava = [813570310574604857083666514280991394838348107239006855762263646490591232]
        self.mode = [815807986147978360186623876533214024184259990226077723278195246141276160]
        self.okx = [812977191747927543008183839949076962963528090061710963167679367065108480]
        self.optimism = [811790954094572914857218491285248099213888055707119177978510808214142976]
        self.orderly = [814540868654622280116274526824124101542599044438218316371583376459563008]
        self.polygon = [811737034201238613577629157255074059952540781418274096833548600993644544] 
        self.viction = [814082549561280719239765187567644767821147212983035126639404615085326336] 
        self.zora = [814055589614613568599970520552557748190473575838612586066923511475077120] 

    
    def get_random_parameter(self):
        all_parameters = [
            self.arbitrum_nowa, self.base, self.bnb, self.fantom, self.gnosis, 
            self.injective_evm, self.kava, self.mode, self.okx, self.optimism,
            self.orderly, self.polygon, self.viction, self.zora
        ]
        return random.choice(all_parameters)
        

    def get_gas_range(self, parameter: str):
        gas_ranges = {
            '[813516390681270555804077180250817355577000832950161774617301439270092800]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[813759030201274911562229183386600532253063567249964639769631371762335744]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[811548314574568559099066488149464922537825321407316312826180875721900032]': (6.0384535007747e-05, 8.0384535007747e-05),
            '[811817914041240065497013158300335118844561692851541718550991911824392192]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[812707592281256036610237169798206766656791718617485557442868330962616320]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[815107027534632443551962534140951513786745424471091668393686552274796544]': (6.0384535007747e-05, 8.0384535007747e-05),
            '[813570310574604857083666514280991394838348107239006855762263646490591232]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[815807986147978360186623876533214024184259990226077723278195246141276160]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[812977191747927543008183839949076962963528090061710963167679367065108480]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[811790954094572914857218491285248099213888055707119177978510808214142976]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[814540868654622280116274526824124101542599044438218316371583376459563008]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[811737034201238613577629157255074059952540781418274096833548600993644544]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[814082549561280719239765187567644767821147212983035126639404615085326336]': (2.0384535007747e-05, 4.0384535007747e-05),
            '[814055589614613568599970520552557748190473575838612586066923511475077120]': (2.0384535007747e-05, 4.0384535007747e-05),
        }
        
        if parameter in gas_ranges:
            gas_min, gas_max = gas_ranges[parameter]
            return random.uniform(gas_min, gas_max)
        else:
            raise ValueError(f"Газ для параметра '{parameter}' не найден.")