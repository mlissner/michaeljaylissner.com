Title: Rsnapshot Backup Solution OR Why Backing Up Is Hard To Do
Date: 2008-12-09T22:06:48
Tags: rsnapshot, archive, backup, project
Category: Tech

I've been working on getting this post figured out for about five months. In this post, I am going to try to explain exactly how my backup works, and why. It's ridiculously complicated at times, but the detail is necessary on paper in some form or other.

For my backup system, I rely heavily on <a href="http://rsnapshot.org">rsnapshot</a>, which is a tool that uses rsync and some perl scripting to create snapshots of directories. Rsync is a pretty awesome tool. It functions like a simple copy/paste, except that it will check the destination directory of the paste and will only copy the necessary rsnapshot. As such, it can be interrupted in the middle of a copy, and will be able to continue later where it left off. Perl is a scripting language that has been used with rsync to give it some extra power.

This power is the ability to perform incremental backups, which is to say that if I have 5GB of data that I backup 10 days in a row, it will only take up about 5GB of data, total. However, if I have 5GB of data today, an additional 5GB tomorrow, and another 5GB the day after, which I backup each day for ten days, it will only require a total of 5GB of space the first day, 10GB the second day, 15GB the third day, and no more space after that for the remaining 7 days.

This is important if you want to backup your data on a regular basis. Since I run a server, I have several things that I must backup. I back these up on a daily, weekly, and monthly basis. The list includes:

 - My laptop is backed up wirelessly to the server's hard drive
 - The email server gets copied to an external USB drive (this includes all the Zimbra configuration rsnapshot as well as thousands of emails)
 - The web server gets backed up to the USB drive (this includes the Drupal installation and the MySQL database)
 - Lots of configuration rsnapshot for the servers go to the USB drive (i.e. the /etc/ directory)
 - And finally, the backup configuration itself goes to the USB drive


Each of these backups presents some challenging difficulties. For the web server, it is challenging because it is backing up MySQL, Zimbra and Drupal. In order to do this, I have to coordinate the MySQL database dump so that when the Drupal backup is triggered, it will copy the MySQL information over to the USB drive along with the normal Drupal information. For Zimbra, the email server has to be stopped, backed up, and then started again, which means control of the email server has to be carefully scripted.

The laptop presents a challenge because it is the only thing that is backed up wirelessly, and in order to do so, the server must authenticate itself to the laptop before it is allowed to log in and make the copies. If that wasn't complicated enough, in addition, the laptop needs to be set up with a static IP address so that the server can find it to perform the backup. Finally, the laptop needs to be ON, and connected to the network when the server attempts the backup. 

Once all of that is figured out logically, you have to authenticate the laptop to the server, create the scripts, backup configurations and cron rsnapshot. I have attached some of these configuration rsnapshot to this post, provided they don't reveal too much of my network topology.

One final challenge that had to be overcome was connecting the USB drive to the server in such a way that it would always be mounted in the same location. In addition, I learned that FAT32 doesn't support file system links, and so I had to format the USB drive as ext3.

As of today, it's about five months since I began this project, and I believe I can say that the backup happens flawlessly on a daily, weekly and monthly basis. There are a few things I'd like to change however:

 - <del>I'd like to get an email notification when a backup fails</del> &mdash; Done - See comment below.
 - <del>I'd like to begin backing up /etc/ on my laptop</del> &mdash; Done
 - <del>At one point, I was backing up a list of all the installed software on my system - it'd be nice to have that again</del> &mdash; Done - I wrote a python script to do so
 - <del>The backup is unencrypted, so anybody can take the USB drive and have a heck of a lot of emails. Gotta fix that.</del> &mdash; See the note below in the comments for details.


**Files of Interest**

1. [rsnapshot configuration for my laptop][1]
1. [rsnapshot configuration for the Drupal server][2]
1. [rsnapshot configuration for the backup configuration rsnapshot and the 
`/etc` directory][3]
1. [rsnapshot configuration for the Zimbra server][4]
1. Scripts to [stop][5] and [start][6] Zimbra
1. My [cron file][7]

All in all, this just goes to show that backing up is a very difficult thing to do properly and automatically. It's one thing if you have a desktop that backs up to a USB drive. It's another if you have a server and a laptop. Had I known how long this would take going into it, I'm not sure I would have figured it all out. How the average computer user is supposed to figure this out is beyond me.

[1]: {filename}/archive/rsnapshot/rsnapshotOpal.conf
[2]: {filename}/archive/rsnapshot/rsnapshotDrupal.conf
[3]: {filename}/archive/rsnapshot/rsnapshotEtcHome.conf
[4]: {filename}/archive/rsnapshot/rsnapshotZimbra.conf
[5]: {filename}/archive/rsnapshot/ZimbraStop 
[6]: {filename}/archive/rsnapshot/ZimbraStart
[7]: {filename}/archive/rsnapshot/cronlist.txt
