Title: Chronicals of installing Zimbra, OR If it looks awesome, it's probably a pain to install.
Date: 2007-09-14T00:24:56
Tags: Linux, zimbra
Category: Tech

First of all, [check this out][1]. Use the username 'admin' and the 
password 'zcsadmin'. When you're done there, come back here, 
and pick up where you left off. 

It's pretty sweet right? Calendar functions, ajaxy goodness, tagging, 
searching, etc. Pretty much all you could want from a web email client, 
right? Right. So I figured I'd download and install it. The first thing that
 worried me was that it wasn't in the repositories of Ubuntu software, 
 so it wasn't just a `sudo aptitude install zimbra` away. So I 
 downloaded it to `/usr/src`, unpacked it, found the install script 
 (`install.sh`), and began the magic (`cd /usr/src/zsc; sudo ./install
 .sh`)

Aside from the fact that my CPU overheated about 20 times while downloading 
the Zimbra Suite (apparently it needed thermal grease and a heat sink 
realignment), all went well until the install script got to resolving my MX 
records, hostname, /etc/hosts file, etc. Apparently figuring these out is a 
bloody pain in the ass (forgive the imagery, I mean it in the British sense)
. So for the past few days I've been struggling with getting this figured 
out, and the point of this post is, if you've been sending emails to any 
@michaeljaylissner.com address, I'm ashamed to say, 
they're not going through. But you probably have realized this, 
because they're bouncing back to you. Well, now you know why.

Give me a couple more days, I'm working on it. In the mean time, 
the [contact][2] link does work.

[1]: http://www.redhatxchange.com/Zimbra.html
[2]: ://michaeljaylissner.com/contact/
