{
    "categories": [
        "windows", 
        "ubuntu", 
        "microsoft", 
        "Linux"
    ], 
    "date": "2008-04-29T21:33:41", 
    "tags": [
        "windows", 
        "ubuntu", 
        "microsoft", 
        "Linux"
    ], 
    "title": "Remap Caps Lock as Backspace in Windows and Linux"
}

A while back my wrist started hurting from reaching for the cursed backspace key. I was making too many mistakes. My solution was to remap the caps lock key on all the computers I use to act as an additional backspace key. How did I do it? Well, I'm glad you asked. I'll tell you.

<strong>In Windows</strong>
EDIT: I noticed that the picture doesn't have all the detail you need. The easier way to do this, is to download the registry key attached to this post, and to right click it, selecting merge. After that, restart the computer, and you should be all set.

To remap the caps lock to function as a backspace key in Windows, one must edit the registry keys. To do that, go to Start > Run..., and type in regedit. In the editor that opens up, navigate to the key shown in the picture below, and create a new key named Scancode Map of the type REG_BINARY. Give it the value shown in the picture, restart, and you're set. If things get wacky, delete the key and try again.

<img src="/files/images/Windows%20Registry%20Remap%20Screenshot.jpg">

<strong>In Linux</strong>
I have tested the following in Ubuntu 7.04, 7.10, 8.04, 8.10, and 9.04. Start by opening a terminal, and running the xev program. Once that is running, press the caps lock key, and it will tell you the numerical value of that key. For example, my output from that command looks like this:<code  lang="bash">
mlissner@opal2% xev
KeyPress event, serial 28, synthetic NO, window 0x4800001,
    root 0x59, subw 0x0, time 2775892, (373,636), root:(376,685),
    state 0x0, <strong>keycode 66</strong> (keysym 0xff08, Caps_Lock), same_screen YES,
    XKeysymToKeycode returns keycode: 22
    XLookupString gives 1 bytes: (08) "
    XmbLookupString gives 1 bytes: (08) "
    XFilterEvent returns: False</code>

In there, you will see the keycode for the capslock key, in my case, number 66. Using that, create a file in your home directory called .Xmodmap, and put the following in it:<blockquote><code>!
! Make the caps lock button a backspace button
!
remove Lock = Caps_Lock
keycode 66 = BackSpace</code></blockquote>

Once that is done, the next time you log in, your caps lock will function as a backspace. The only remaining problem is that it still does not have the auto-repeat function that backspace should have. To fix that, run:<code lang="bash">
xset r 66</code>
That will make things work properly, but you need to run that every time you log in, or else it won't work properly. To fix that run:<code lang="bash">
sudo gedit /etc/X11/Xsession.d/50x11-common_determine-startup</code>
And add xset r 66 to the bottom.

That should do it.

Source: http://ubuntuforums.org/showthread.php?t=369402
<!--break-->
