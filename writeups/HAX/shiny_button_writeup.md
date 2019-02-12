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

a';cat flag.txt <-- No response
a;cat flag.txt <-- a\n <hash of 'cat flag.txt'>

So closing the string breaks the script,
we are echoing 'a' and the rest is being passed into md5sum
To me, the command runs on the server like:
    echo <input> | md5sum

So how can we exploit that?
a;cat flag.txt;echo a <-- only give'a' and the hash of 'a'. Completely skips the cat flag command

The reason for the <cmd>;echo a is because we need to:
finish the echo command first
Run our command
and finally feed some input (not the output of our command) into md5sum so we just send garbage data

Lets try just a normal command rather than reading a filename
`ls`;echo a <-- Now we're getting something!
The `` tell bash to evaluate whats between the ticks and feed the output to echo
We see Cerulean_Cave so lets enumerate
`ls Cerulean_Cave`;echo a
RESULT: MewTwo.txt

Cool! lets read it!

SOLVE:
`cat Cerulean_Cave/MewTwo.txt`;echo a
