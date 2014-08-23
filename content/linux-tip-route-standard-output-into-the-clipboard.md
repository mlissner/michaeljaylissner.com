Title: Linux Tip - Route Standard Output Into to the Clipboard
Date: 2008-08-28T20:47:05
Tags: Linux, CLI
Category: Tech


A friendly online stranger just taught me how to do something that has been plaguing me for some time. Ever since I learned how to use pipes in the unix commandline, I have wanted to know how to pipe the output of a command into the system clipboard.

For example, the echo command simply repeats whatever you tell it to. So if I run
 
    :::bash
    echo hello

The computer will give me the output 
    
    :::bash
    hello 

By using a pipe (this symbol: |) I can route the output of one command into the input of another. 

For example, if I run: 

    :::bash
    echo hello | helloprogram

The helloprogram will receive the value of 'hello' as an input, and will do something with it. This allows stringing together small commands into long ones, which sometimes is incredibly handy. 

Anyway, if you want to route standard output into the system clipboard, you will need to install an application called xclip. Once that is installed, a command such as:

    :::bash
    echo hello | xclip -i -selection clipboard

Will put the word hello into the clipboard. Ctrl + V will then paste that 
value into whatever application desired.

Thanks to aaron at <a href="http://www.cyberciti.biz/faq/linux-copying-with-middle-mouse-button/#comment-38676">http://www.cyberciti.biz/faq/linux-copying-with-middle-mouse-button/#comment-38676</a> for help with this question.
