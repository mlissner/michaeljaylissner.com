Title: Notes on Drupal Multisite
Date: 2008-03-05T23:23:24
Tags: drupal
Category: Tech

As I mentioned in my previous post, I just finished setting up a drupal multisite configuration. It took a lot of work to get this all figured out, so I thought I would put some notes together for those that may follow in my footsteps.

What challenged me the most with figuring this out were the concepts, so I want to touch on those more than anything else.

The way to set up a multisite installation consists of the following general steps:

1. Make a new drupal database in your MySQL install
1. Set up the directory hierarchy in your drupal directory
1. Set up your second domain as a virtual host in apache
1. Configure your settings.php file to point to your new database
1. Run the install.php script from your browser

That's really it, but it's kind of a complicated process. Some further 
notes expanding the concepts from above:

1. When you're making your new MySQL database, I found the command line to 
be the easiest way to do it, but there are a lot of instructions on how to 
do it with web-based tools. For a good tutorial on the command line method 
check this out <a href="http://drupal.org/node/22675" target="_blank">http://drupal.org/node/22675</a>.

2. The directory hierarchy was one of the more complicated parts of this for 
some reason. Essentially, it should look like this:

    :::bash
    drupal/sites/default
    drupal/sites/site1.com
    drupal/sites/site2.com

Within site1.com and site2.com go your settings.php and dbconfig.php files.
If you like, you can put modules and themes directories as well. If you do, 
drupal will use these modules/themes if there is not a module/theme of the 
same name in the usual directory. This is really useful because it allows 
modules to be installed on one site, the other or both, 
depending on where you put the module's directory.

3. I can't remember exactly how I set up the virtual hosts, 
but the Internet has many resources on this one. The trick to know is that 
one virtual host points to the drupal/sites/site1.com directory, 
and the other points to the drupal/sites/site2.com directory.

4. No tricks here or on number five.

Good luck! 
