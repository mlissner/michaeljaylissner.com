Title: Install Citrix In Ubuntu Hardy Heron
Date: 2008-06-02T09:44:53
Tags: Linux, ubuntu, citrix
Category: Tech

For a while there, I was struggling to get the Citrix client installed on 
my computer. It was frustrating, and I put hours into debugging it, 
and trying to get it to work. In the end, I took a circuitous route, 
installing VirtualBox in Ubuntu, Windows in VirtualBox, Firefox in Windows,
and finally Citrix in Firefox.

Last week, I took another stab at getting this done, and for some reason it
went very smoothly. To install Citrix in Ubuntu Hardy Heron, begin by 
[downloading][1] the Citrix client as a .tar.gz.

Next, unpack the install file using the terminal by running: 
 
    :::bash
    sudo tar xvfz en.linuxx86.tar.gz

Change into the Citrix directory, and run 
 
    :::bash
    sudo ./setupwfc

This will begin the install script. As it proceeds, 
simply allow the default settings, and you should be good.
    
The final step is to install the root certificates. To do this, 
attempt to start a Citrix program, and it may fail, 
reporting an error message. In the message, it will tell you what 
certificates it needs installed. Go to [this website][2], and download the 
certificates the error message informed you that you need by right clicking 
their download links, and selecting "Save as..." Once those are downloaded,
rename their extension so they are .crt files, and move them to 
 
 :::bash
 /usr/lib/ICAClient/keystore/cacerts
 
Restart Firefox, and you should be good.

Thanks to [Skarh][3] for this how to.

[1]: http://www.citrix.com/English/ss/downloads/details.asp?downloadId=3323&productId=186&c1=ost1349860#top
[2]: https://www.geotrust.com/resources/root_certificates/index.asp
[3]: http://skarh.wordpress.com/2008/05/20/how-to-citrix-on-ubuntu/
