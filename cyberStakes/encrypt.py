#!/usr/bin/env python3

import base64
import binascii
import os
import sys

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import gmpy2
from gmpy2 import mpz

if len(sys.argv) < 3:
    print("Usage: {} <message to encrypt> <encryption passphrase>".format(sys.argv[0]))
    sys.exit(1)
message = sys.argv[1].encode()
passphrase = sys.argv[2]

key = os.urandom(16)
nonce = b'0000000000000004'  # Chosen by fair dice roll. Guaranteed to be random.
cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
encryptor = cipher.encryptor()
ct = encryptor.update(message) + encryptor.finalize()

h, q, g, G, p, x = [mpz(v, 16) for v in base64.b64decode(passphrase).split(b':')]
m = h*p + gmpy2.invert(q, p) + G
k = mpz(binascii.b2a_hex(key), 16)
z = gmpy2.powmod(k, g, m)
for i in range(x):
    k = (k * k) % m

print('{:x}:{}'.format((z*k) % m, binascii.b2a_hex(ct).decode()))
