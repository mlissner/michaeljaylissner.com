Title: Drag a Screenshot Using ImageMagick
Date: 2008-05-17T17:48:40
Tags: Linux, imageMagick
Category: Tech


I learned an interesting trick while working on the Fuji water article. We all know that if you want to take a screenshot in Linux, all you usually have to do is press the "printscreen" button. That, however, takes a screenshot of the entire screen, which you then have to trim down into a useful bit of picture. 

The trick I learned to make this easy is to simply type:

    :::bash
    import screenshot.png

That will turn your cursor into a little crosshair, which you can drag across a section of the screen. 

If you want to do that after a delay, the trick is to use the sleep command like so:

    :::bash"
    sleep 10; import screenshot.png

I found this tip along with a lot of others on <a href="http://tips.webdesign10.com/how-to-take-a-screenshot-on-ubuntu-linux">this blog</a>. There are some other interesting techniques there as well.
