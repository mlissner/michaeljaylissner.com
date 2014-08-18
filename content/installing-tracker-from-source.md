Title: Installing Tracker from Source
Date: 2009-02-23T00:13:40
Tags: Tracker, install, howto, desktop search
Category: Tech

I've been working over the past several weeks on getting Tracker to work better on my system. There are a couple reasons that I'm doing this. The first is that by default on Ubuntu, Tracker doesn't support a number of meta formats (such as the tags in JPEGs, ID3 info in MP3s, and the like). The second was that the RDF parsing code in the default Ubuntu version is a bit buggy, and the new version is better. It's been a bit of a pain figuring out the install process, so I figured I'd post here so others might have an easier time.

The <a href="http://projects.gnome.org/tracker/start.html" target="_blank">online instructions</a> say to simply download the code, and to install it. No big deal, right? Well...in reality, it's a bit harder than that. The process I went through was to download the source from <a href="http://projects.gnome.org/tracker/download.html" target="_blank">here</a> per the instructions, unpack the source files, and to run the configure command. 

After the configure command is run each time, it will give you a summary of which components will be installed, and which will not. If you have all the dependencies necessary, and include a couple of arguments to the configure command, everything will get installed. If not, certain pieces will be missing. 

The list of dependencies is a bit long, so before you run ./configure, you might as well install them. To do so, run:

<code lang="bash">
sudo aptitude install libgmime-2.0-2a libgmime-2.0-2-dev dbus-glib-1-dev libdbus-glib-1-dev libhal-dev libhal-storage-dev sqlite3-dev libsqlite3-dev libexif-dev libdeskbar-tracker libgsf-1-dev libjpeg62-dev libtiff4-dev libxine-dev libpoppler-dev libgstreamer0.10-dev libpoppler-glib-dev libtotem-plparser-dev libunac1-dev libexempi-dev libraptor1-dev libtracker-gtk-dev libgnome-desktop-dev libgnome-desktop-dev libnotify-dev</code>

Once those are installed, run:
<code lang="bash">
 ./configure --enable-deskbar-applet --enable-tracker-applet --prefix=/usr --sysconfdir=/etc</code>

After this, it should say that pretty much everything will be installed. If so, you can proceed to the commands below, and once those are complete, the latest version should be installed with full functionality.<code lang="bash">make
sudo make install</code>

If after running your configure script (<code lang="bash">./configure</code>) it doesn't indicate that everything will be installed, put in a comment below, and we'll see what we can do.
