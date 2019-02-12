from pwn import *

r = remote('challenge.acictf.com', 31802)

r.recvuntil('--------------------------------------------------------------------------------')

while(1):
    direction = r.recv().strip()
    print(direction)
    if(direction == 'left'):
        resp = '<'
    elif(direction == 'right'):
        resp = '>'
    elif(direction == 'down'):
        resp = 'V'
    else :
        resp = '^'
    print("sending: {}".format(resp))
    r.send(resp)
    print("sent!")
    print(r.recvline())
