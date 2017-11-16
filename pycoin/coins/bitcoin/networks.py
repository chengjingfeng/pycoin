
from pycoin.serialize import h2b

from .ScriptTools import BitcoinScriptTools
from .Tx import Tx as BitcoinTx
from pycoin.block import Block as BitcoinBlock

from pycoin.ecdsa.secp256k1 import secp256k1_generator
from pycoin.networks.network import Network
from pycoin.ui.uiclass import UI
from pycoin.vm.PayTo import PayTo

# BRAIN DAMAGE
_puzzle_script = PayTo(BitcoinScriptTools)

# BRAIN DAMAGE
mainnet_ui = UI(
    _puzzle_script, secp256k1_generator,
    bip32_prv_prefix=h2b("0488ade4"), bip32_pub_prefix=h2b("0488B21E"),
    wif_prefix=h2b("80"), sec_prefix="BTCSEC:", address_prefix=h2b("00"),
    pay_to_script_prefix=h2b("05"), bech32_hrp='bc')

BitcoinMainnet = Network(
    'BTC', "Bitcoin", "mainnet",
    BitcoinTx, BitcoinBlock,
    h2b('F9BEB4D9'), 8333, [
        "seed.bitcoin.sipa.be", "dnsseed.bitcoin.dashjr.org",
        "bitseed.xf2.org", "dnsseed.bluematt.me",
    ],
    ui=mainnet_ui
)

testnet_ui = UI(
    _puzzle_script, secp256k1_generator,
    bip32_prv_prefix=h2b("04358394"), bip32_pub_prefix=h2b("043587CF"),
    wif_prefix=h2b("ef"), sec_prefix="XTNSEC:", address_prefix=h2b("6f"),
    pay_to_script_prefix=h2b("c4"), bech32_hrp='tb')

BitcoinTestnet = Network(
    "XTN", "Bitcoin", "testnet3",
    BitcoinTx, BitcoinBlock,
    h2b('0B110907'), 18333, [
        "bitcoin.petertodd.org", "testnet-seed.bitcoin.petertodd.org",
        "bluematt.me", "testnet-seed.bluematt.me"
    ],
    ui=testnet_ui
)