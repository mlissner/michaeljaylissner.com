Title: Install Garmin Topo! in Linux
Date: 2008-02-11T22:08:23
Tags: Linux, camping
Category: Tech

I'm planning a quick trip out to Yosemite for next weekend, and I wanted to print out a couple of maps from Garmin Topo! beforehand. The last time I used Topo! was about four years ago, when I had Windows XP installed. I don't remember how I installed it then, but that probably means it wasn't too challenging. 

This time, however, I don't have a computer running Windows except for as a virtual client within Ubuntu, so I figured that would be the best place to begin. I booted up Windows XP, popped in the CD, mounted it within the virtual client, and tried to install. No dice: some error message. I played with it for a while, and I eventually decided that for some reason, it just wasn't going to work. 

My next idea was to try installing Topo! within Ubuntu via Wine (Wine Is Not an Emulator). Wine is an application that attempts (and often fails, sometimes works) to allow Windows applications a method of working within Linux. I closed down Windows, opened the install CD within Ubuntu, and double-clicked the Setup.exe file. Amazingly, the Windows Install Shield business popped up, and the installation proceeded with no problems whatsoever.

Once that was done, the only remaining step was to make myself a nice link/alias/launcher. Once it's installed, the Topo! executable is located at ~/.wine/drive_c/TOPO!/TOPO.EXE, so it's just a matter of making a link to that, and you're all done.
