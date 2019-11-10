# Brain wallet
# using pybitcointools (https://pypi.python.org/pypi/bitcoin) by vitalic
# 2018. 11. 3

import bitcoin.main as btc

passphrase = "Brain Wallet passphrase"
privKey = btc.sha256(passphrase)
dPrivKey = btc.decode_privkey(privKey, 'hex')
#if dPrivKey < btc.N:
#    break


# generating from private key to public key 
pubKey = btc.privkey_to_pubkey(privKey)

# from public key to Mainnet wallet address (prefix : 0x00)
address1 = btc.pubkey_to_address(pubKey, 0x00)

# public key => Testnet wallet address (prefix : 0x6f)
address3 = btc.pubkey_to_address(pubKey, 0x6f)

print("\npassphrase \n ", passphrase)
print("\nprivate key using passphrase:\n ", privKey, len(privKey))
print("\npublic key \n ", pubKey, len(pubKey))
print("\nMainnet wallet address \n ", address1, len(address1))
print("\nTestnet address \n ", address3, len(address3))


