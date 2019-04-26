import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

def int_of_string(s):
    return int(binascii.hexlify(s), 16)


def encrypt(key, ptxt):
    # iv = os.urandom(16)
    iv_hex = '5A557AC90890B2ACD59C536FE4279BBC'
    iv_bin = bytes.fromhex(iv_hex)
    ctr = Counter.new(128, initial_value=int_of_string(iv_bin))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv_bin + aes.encrypt(ptxt)


def decrypt(key, ctxt):
    iv = ctxt[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ctxt[16:])


def main():
    # key = os.urandom(16)
    key = '5A557AC90890B2ACD59C536FE4279BBC'

    while(1):
        choice = int(input('1: encrypt\n2: decrypt\n3: exit\n'))
        if(choice == 1):
            msg = input('enter string to encrypt\n')
            ctxt = encrypt(key, msg)
            print('ciphertext:\t', ctxt.hex())
        if(choice == 2):
            msg = input('enter hex to decrypt\n')
            ptxt = decrypt(key, bytes.fromhex(msg))
            print('message:\t', ptxt)
        if(choice == 3):
            break


if __name__ == '__main__':
    main()
