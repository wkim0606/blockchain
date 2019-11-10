# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
# you have to install bitcoin package using "pip install bitcoin
# ECDSA Test by wkim, 2019. 11. 09

import bitcoin.main as btc

d=btc.random_key()
Q=btc.privkey_to_pubkey(d)
G=btc.getG()
Gx=int(G[0])
Gy=int(G[1])

print("\n === d * G(x,y) = Q (x,y) ===\n")
print("\n ===Random_key : Private Key(d)=== \n\n", d, "\n\n ===PrivKey Length(hexa)===\n", len(d))
print("\n ===Gx == \n", Gx)
print("\n ===Generator(Gx)=== \n", G[0])
#print("\n ===Len Gx===", len(Gx))
print("\n ===Generator(Gy)=== \n", G[1])
#print("\n ===Len Gy===", int(len(G[1])))
print("\n ===Public Key Q=d*G=== \n", Q,"\n\n ===Pubkey Len(hexa)===", len(Q))

message="The input text message for testing ECDSA"

en_m=message.encode()
print("\n ===the result to encode this message===\n", en_m)

v,r,s=btc.ecdsa_raw_sign(btc.electrum_sig_hash(en_m),d)
print("\n ===ECDSA raw Signature Result(v)=== \n", v)
print("\n ===ECDSA raw Signature Result(r)=== \n", r)
print("\n ===ECDSA Signature Result(s)=== \n", s)

sig1=btc.encode_sig(v,r,s)
print("\n===Signature Result(sig1)===\n", sig1)
sig2=btc.ecdsa_sign(en_m,d)
print("\n ===Signature Result(sig2)=== \n", sig2)

v=btc.ecdsa_verify(en_m,sig2,Q)
print("\n===v's value===\t", v)

print("\nMessage =", en_m.decode())
if v:
    print("\n Valid Signature")
else:
    print("\n Invalid Signature") 


passphrase = 'Brain wallet\'s test private key. forget it'
privKey = btc.sha256(passphrase)
dprivkey = btc.decode_privkey(privKey, 'hex')

print("\n === PassPhrase ====\n", passphrase) 
print("\n === privKey ====\n", privKey) 
print("\n === decimal of privkey ====\n", dprivkey) 

input("\n\n\t\t if you wanna stop it, pls enter")

