#!/usr/bin/python

from pwn import *

r = remote('challenge.acictf.com', 1751)

r.recvuntil(': ')
encrypted = r.recv().strip()
print(encrypted)
print(len(encrypted))

IV = encrypted[0]
