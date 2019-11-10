# package : pybitcointools (https://pypi.python.org/pypi/bitcoin written by vitalik
# private key generation by wkim, 2018. 11. 03

import bitcoin.main as btc

#d=btc.random_key()
#Q=btc.privkey_to_pubkey(d)
#G=btc.getG()
#Gx=int(G[0])
#print("\n ===Private Key(d)=== \n", d, "\n ===PrivKey Length===", len(d))
#print("\t ===Gx == \t", Gx)
#print("\n ===Generator(Gx)=== \n", G[0])
#print("\n ===Generator(Gy)=== \n", G[1], "\n ===Len Gy===", int(len(G[1])))
#print("\n ===Public Key Q=d*G=== \n", Q,"\n ===Pubkey Len===", len(Q))

#message="본 메시지는 ECDSA를 테스트하기 위한 문서 원본이다."

#en_m=message.encode()
#print("\n ===문서 인코딩한 결과 출력===\n", en_m)

#v,r,s=btc.ecdsa_raw_sign(btc.electrum_sig_hash(en_m),d)
#print("\n ===ECDSA raw Signature Result(v)=== \n", v)
#print("\n ===ECDSA raw Signature Result(r)=== \n", r)
#print("\n ===ECDSA Signature Result(s)=== \n", s)

#sig1=btc.encode_sig(v,r,s)
#print("\n===Signature Result(sig1)===\n", sig1)

#sig2=btc.ecdsa_sign(en_m,d)
#print("\n ===Signature Result(sig2)=== \n", sig2)

#v=btc.ecdsa_verify(en_m,sig2,Q)
#print("\n===v's value===\t", v)
#
#print("\nMessage =", en_m.decode())
#if v:
#    print("\n Valid Signature")
#else:
#    print("\n Invalid Signature") 


#passphrase = 'Brain wallet\'s test private key. forget it'
#privKey = btc.sha256(passphrase)
#dprivkey = btc.decode_privkey(privKey, 'hex')

#print("\n === PassPhrase ====\n", passphrase) 
#print("\n === privKey ====\n", privKey) 
#print("\n === decimal of privkey ====\n", dprivkey) 

import os
import random
import time
import hashlib

# secp256k1의 domain paramter (order of G)
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337

# CSPRNG : os.urandom(), random() 
def random_key():
    r = str(os.urandom(32)) \
            + str(random.randrange(2**256)) \
            + str(int(time.time() * 1000000))
    r = bytes(r, 'utf-8')
    h = hashlib.sha256(r).digest()
    key = ''.join('{:02x}'.format(y) for y in h)
    return key


privkey = random_key()
print("\n === privKey Generation ====\n", privkey) 

input("\n\n\t\t if you wanna stop it, pls enter")
