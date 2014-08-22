Title: Old Versions of Site are Up...sort of...
Date: 2007-10-11T19:04:42
Tags: blog, me
Category: Tech

I was working on getting the <a href="http://michaeljaylissner.com/archive/oldsite" title="Old Site">old versions</a> of the site up and going for history's sake, and I have more or less accomplished the task, though I learned a very important lesson in the process.

For one, I learned that if you want to host additional custom directories on your drupal site, it's a piece of cake: Just make the directories in your drupal directory, and you're done. For example, my drupal directory is at /usr/share/drupal-5.1, so to host a page at michaeljaylissner.com/oldsite, I just made a directory at
/usr/share/drupal-5.1/oldsite, put stuff in it, and was done.

The more important lesson was that when hand-coding HTML, as I did in the previous version of the site, relative links such as /assets/picture1.jpg are <strong>NOT</strong> the same as relative links such as assets/picture1.jpg. Both work, but only one is actually relative to the current page (the latter one). The former one may as well have been written michaeljaylissner.com/assets/picture1.jpg, because that's what that first slash means. Duh.

Somehow, I never ran into this problem before now. Anyway, if you take the time to check out the old site (which I don't really recommend), you'll find many broken links. This is why.
The other project I have been working on is getting all of my pictures from the old site set up on this site in a place where registered users can find them. This is a work in progress, but if you're a registered user, you might be interested to see them, if you haven't already. 
