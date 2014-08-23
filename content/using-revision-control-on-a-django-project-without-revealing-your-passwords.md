Title: Using Revision Control on a Django Project Without Revealing Your Passwords
Date: 2010-02-24T17:15:54
Tags: settings.py, revision control, Python, mercurial, django, Final Project
Category: Tech

Just a quick post today, since this took me way too long to figure out. If you have a django project that you want to share without sharing the private bits of settings.py, there is an easy way to do this. 

I tried for a while to to set up mercurial hooks that would strip out my passwords before each commit, and then place them back after each commit, thus avoiding uploading them publicly. This does not work however because all of the mercurial hooks happen after snapshots of the modified files have been made. So you can edit the files using a hook, but your edits will only go into effect upon the <em>**next**</em> check in. Clearly, this will not do.

Another solution that I tried was the mercurial <a href="http://mercurial.selenic.com/wiki/KeywordExtension">keyword extension</a>. This could work, but ultimately it does not because you have to remember to run it before and after each commit &mdash; something I know I'd forget sooner or later.

The solution that <em>**does**</em> work is to split up your settings.py file into multiple pieces such that there is a private file and a public file. I followed the instructions <a href="http://code.djangoproject.com/wiki/SplitSettings#UsingalistofconffilesTransifex">here</a>, with the resulting code looking being checked in <a href="http://bitbucket.org/mlissner/legal-current-awareness/src/fa5cc7fb9c0b/alert/settings.py">here</a> and <a href="http://bitbucket.org/mlissner/legal-current-awareness/src/fa5cc7fb9c0b/alert/settings/">here</a>. There is also a file called "20-private.conf" which is not uploaded publicly, and which contains all the private bits of code that would normally be found in settings.py. Thus, all of my settings can be found my django, but I do not have to share my private ones.
