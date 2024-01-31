# Для пользователей чата Bitcoin_Rishes
# одификации и улучшения приветствуются
# А мне просто некогда )))

from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy
from web3 import Web3, HTTPProvider

PASSPHRASE = None
LANGUAGE ="english" # chinese_simplified, chinese_traditional, english

w3 = Web3(Web3.HTTPProvider('http://173.212.227.224:8545'))

def balance():
     get_balance = w3.eth.get_balance(address)
     return get_balance

def transaction():
     get_transaction = w3.eth.get_transaction_count(address)
     return get_transaction


while True:
     ENTROPY = generate_entropy(strength=128)
     wallet = Wallet()
     wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)
     wallet.from_index(44,harden=True)
     wallet.from_index(60, harden=True)
     wallet.from_index(0, harden=True)
     wallet.from_index(0)
     wallet.from_index(0, harden=True)
     address = wallet.address()
     priv = wallet.private_key()
     mnemonic = wallet.mnemonic()
     priv_imp = wallet.wallet_import_format()
     
     print("Address: ", address, "Transactions: ", transaction()) #, "Balance: ", balance(), mnemonic)

     if transaction() != 0:
          file = open("found.txt", "a")
          file.write("Address: " + address + "\n" +
                     "PrivKey: " + priv + "\n" +
                     "PrivImp: " + priv_imp + "\n" +
                     "Mnemonic: " + mnemonic + "\n" +
                     "==================================================" + "\n" + "\n")
          file.close()
