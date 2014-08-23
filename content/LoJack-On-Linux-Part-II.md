Title: LoJack for Linux Part II
Date: 2007-09-25T22:42:45
Tags: Linux, security, lojack
Category: Tech

EDIT: See update in the comments

I did some <a href="http://www.arsgeek.com/?p=1612">research</a> after that last post, and I learned that the trick to this is to get a free account from dyndns.com, and then use the ddclient in daemon mode. That combination will allow you to track the IP of your computer no matter where it is, no script involved. 

The other piece of this puzzle is somewhat more puzzling: How to access the computer after it is stolen. Ideally, this would happen via ssh, but in practice ssh almost always talks over port 22, and routers pretty much always block all ports. The only solution to this problem I can think of is to hack the thief's router once you know its IP address, but that's hardly a solution really.

The other caveat to consider is that if you need a password to log in, the ddclient won't get started in the first place because the thief won't be able to log in. So, what's the better solution: A password login, or ddclient? 

Hmmm....any solutions to the ssh problem are more than welcome.
