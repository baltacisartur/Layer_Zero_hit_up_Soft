import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
GAS_ZIP_ABI = os.path.join(ABIS_DIR, 'gas_zip.json')

arb_rpc = 'https://arbitrum.llamarpc.com'
eth_rpc = 'https://eth.llamarpc.com'

