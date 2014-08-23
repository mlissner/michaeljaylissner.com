Title: LoJack for Linux
Date: 2007-09-23T14:56:19
Tags: Linux
Category: Tech

I have been spending some time lately shopping for laptops, and I noticed an interesting product on the shelves these days: <i>LoJack for Laptops</i>. It's an interesting concept, because I think LoJack could do a lot of cool things these days for just about anything you buy that's worth more than a couple hundred bucks. My bike, for example, would be another object I would want LoJack for if the system were cheaper. 

I checked out the LoJack installation software, figuring it would inform me that I had to have a GPS chip installed in my laptop for it to work, but to my surprise, it just uses IP addresses. From what I could figure out, it works in two ways. One, it sends your IP address to a centralized server at some regular interval. Two, it allows a back door entrance into your computer so that if your computer is stolen, you can monitor the location of it more closely, bug the new owner, convince them to give it back, etc.

I got to thinking about this, and from what I can tell, there isn't anything here that a Linux laptop can't easily accomplish. The only tricky part I can think of is the back door thing, because I imagine most routers block incoming traffic on pretty much every port except 80, so ssh'ing into the computer might be tricky even once you know the correct IP to use.

As for determining the external IP, I found <a href="http://linux.byexamples.com/archives/307/what-is-my-public-ip-address/">this site</a>, which pretty much fits the bill. The basic idea is to go to one of the million whatsmyip.com-type websites via command line, and grep the IP out of the code. One hilarious thing I found on there was <a href="http://www.moanmyip.com">moanmyip.com</a>. I highly recommend a visit if you're "visually impaired".

Anyway, now that the men in the room are good and turned on, the script pretty much needs three more things: 1. A centralized server to collect the IPs, 2. That ssh back door to mess with the thief, and 3. The script itself!

Updates to come.
