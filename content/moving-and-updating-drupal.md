Title: Moving and Updating Drupal
Date: 2008-07-24T22:45:32
Tags: drupal, apache2
Category: Tech

You may recall from one of my earlier posts that I was running two servers in my attic when I originally set things up at the end of last summer. Originally, I had one server for Zimbra, and the other for Drupal. I did this because I was scared that if I didn't, people would be unable to access the website without getting the email, and vice versa. I had no familiarity with apache, and a limited understanding of ports. 

Well, today I had a moment of inspiration, and decided it was time to retire the older of the two servers, and to move the Drupal installation to the Zimbra server.

In addition to reducing the number of servers that I am maintaining, this also reduces the amount of energy I'm consuming, and also allowed me to update my Drupal installation. I was running Drupal 5.3 because that was the one that was in the Ubuntu repos, but I am now up to 5.9 (the most recent version).

So, how did it go? It went pretty well. I had a backup of everything on my second server already, so it was largely a matter of copying things to the right places. Probably the most important lesson I learned is that symbolic links are not followed by rsnapshot, so my backups until this time have been incomplete. In my new installation, I am not using symbolic links, so that problem should be alleviated.

Another challenge I encountered was that I had to update my dbconfig.php files to line up with the new database configuration, and I also had to spend some time getting the correct document root to function in apache2, which I also just installed.

The biggest problem I encountered was that the clean URL's broke, and were a pain to get fixed. I have fixed those now, so the only remaining thing is to get gallery functioning again. The thing to remember here is that clean urls function by directory, and that the higher up the directory tree you go, the higher the priority of the .htacces files.

As for Gallery2, I have to say it is a big pain, so I may just revert to trusting Google with my images. We'll see if I have another moment of inspiration.
