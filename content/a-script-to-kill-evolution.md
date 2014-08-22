Title: A Script to Kill Evolution
Date: 2008-10-13T17:36:05
Tags: evolution, bash
Category: Tech


I use Evolution as my mail reader, and I like it. It has a lot of good features including a calendar, address book, memos and mail, as well as a number of others. One problem though is that it gets caught up when processing mail, and sometimes just won't come back.

The other problem is that it has several helper apps that are behind the scenes making things work properly, so if you try to just kill the application itself, those will still be running and your problem may not be solved.

My solution was to write a short script to kill all of Evolution and its helper apps. Hope this helps somebody else someday:

    ::: bash
    % more bin/evokill 
    #!/bin/bash
    
    ps aux | grep evolution
    kill `ps aux | grep evolution | awk -F' ' '{print $2}'`

This script just looks for any application that has the word evolution in its name, and then sends it the kill signal. Not too sophisticated, but it gets the job done. You could easily substitute the word evolution for something else as well.
