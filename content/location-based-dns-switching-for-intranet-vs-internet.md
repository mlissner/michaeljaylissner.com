Title: Location Based DNS Switching For Internet vs. Intranet
Date: 2009-02-19T20:45:10
Tags: script, project, /etc/hosts, networking, DNS
Category: Tech

I realized over the weekend that since I run my own mail server out of my 
home, I can configure my computer to download my mail over the intranet 
whenever I am on my home network. By doing this, I can drastically reduce my
mail download times because it cuts the Internet out of the equation. Rather
than using DNS + the Internet to get my mail, I can download it directly 
from internal IP address of the server. 

To understand how to set this up, you have to understand that whenever you 
use a domain name (like michaeljaylissner.com), your computer does an IP 
lookup. First, it looks in /etc/hosts to see if it knows the IP of the 
domain locally. If it does, it will use the IP listed there. If it does 
not, it will ask your Internet provider what IP to use, 
and will use that. Thus, what we want to do is set up the computer so that 
when we are at home, /etc/hosts provides the internal IP of our server, 
and so when we are not at home, it does not.

When I am at home, I am always on a wireless network called, 
`pizzapuppysantaclaus`. Thus, by checking what wireless network I am 
connected to, I can check if I am at home, and make whatever changes are 
necessary. Conveniently, whenever you change network connections, 
you run all of the scripts located in `/etc/network/if-up.d/`. Thus, 
we will put a small script in there that checks what wireless network we are
 on, and then changes our /etc/hosts file if necessary.

To set up this configuration, I made three files. The first is the script 
mentioned above, which needs to be owned by root, 
and placed in `/etc/network/if-up.d`. You can name it whatever you want, 
and by changing `pizzapuppysantaclaus` to the name of your network, 
you can fit it to your needs. Here's the contents of the script:

    :::bash
    #First, we check if we are connected to pizzapuppysantaclaus
    
    #If grep has a hit, we're connected, and $? will equal 0, if not, $? will equal 1
    iwconfig 2> /dev/null | grep pizzapuppysantaclaus > /dev/null
    
    if [ $? = 0 ]
    then
      #Switch the /etc/hosts file with the other one
      cp -f /etc/hostsIntranet /etc/hosts
    
      else
      #Switch the /etc/hosts file with the other one
      cp -f /etc/hostsInternet /etc/hosts
    
    fi
    
    exit 0

This script simply performs a check of our wireless ID. If it's 
`pizzapuppysantaclaus`, it switches `/etc/hostsIntranet` for `/etc/hosts`. If 
not, it switches `/etc/hostsInternet` for `/etc/hosts`.

The contents of `/etc/hostsIntranet` are:

    :::bash
    192.168.1.132	michaeljaylissner.com
    192.168.1.132	charityhikers.org
    127.0.0.1	localhost
    127.0.1.1	opal

    # The following lines are desirable for IPv6 capable hosts
    ::1     localhost ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    ff02::3 ip6-allhosts
    
And `/etc/hostsInternet` is just a copy of `/etc/hosts`. 

So, to make this whole thing run, put the script in `/etc/network/if-up.d`, 
and set its owner to root with execute permission. Create a file called 
`/etc/hostsIntranet`, that contains your intranet configuration, 
as shown above. Make a copy of your normal `/etc/hosts` file called 
`/etc/hostsInternet`. 

Once all that's done, you should be all set. Any questions, 
please feel free to comment!
