Title: Making Prey of Computer Thieves
Date: 2009-07-25T22:39:35
Tags: security, prey
Category: Privacy and Security

Laptops get stolen. It sucks, but we know it happens from time to time. Recently, I've been checking out programs that can help to catch the thieves (and dabbling in writing my own).

One program that I found, called <a href="http://preyproject.com" target="_blank">Prey</a>, helps to do just this. Once installed, every few minutes it will check a website to see if a page exists. If that page exists, it will collect a bunch of information about the computer, and send that (using SMTP of your choice) to an email address of your choice.

So, for example, if I set up a web page at http://michaeljaylissner.com/laptop-stolen, in a few minutes, Prey will see that page, and will collect the following information:

 - The IP address where my computer is connected (this is almost as good as the thief's physical address)
 - The name of the wireless network my computer is connected to, and a list of the others in the area
 - The MAC address of the wireless router my computer is connected to
 - How long my computer has been on (uptime)
 - Any files that have been modified in the last X minutes
 - Any programs that are currently running
 - Any open connections to websites or online services
 - A picture of the thief, if you have a webcam enabled
 - And best of all, a screenshot at the time of the report


Once I get the email with all this information, it's just a matter of taking it to the police, and convincing them to take action on it. 

Of course, all of this could be useless if the thief decides to immediately wipe the data on the computer, but it's a good safeguard that can weed out the dumb thieves at least.

EDIT: Forgot to mention the webcam on the first version.
