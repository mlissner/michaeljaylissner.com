Title: Testing Deletion Speed of Online Photo Sites
Date: 2009-11-14T16:28:44
Tags: Walmart, Twitpic, Shutterfly, service, right to delete, privacy, Picassa, Photobucket, photo, Orkut, MySpace, google, Flickr, facebook, delete
Category: Tech

[TOC]

## Updates

 - **2014-08-22**: While updating this blog to a new platform, 
I wound down these tests and put notes about each service's final result. 
After nearly five years, some of these sites still haven't taken down the 
image.
 - **2010-03-08**: Added an image at drop.io
 - **2010-01-28**: Added an image at Orkut.com
 - **2010-01-28**: At [the FTC privacy round table][ftc] today, 
Facebook's director of public policy, Tim Sparapani, claimed that information 
deleted from Facebook cannot be retrieved even by Facebook staff, 
because it is almost instantly deleted. I informed him this was not true in
the case of pictures, and he said he would look into it. Will update this 
post when/if I hear more.

## Background and Threat Model 

Imagine an embarrassing photo of you is placed online by one of your 
friends. You ask them to take it down, and they do. Now, 
imagine that your enemy had gotten a link to that photo, 
and had posted it to their blog. You'd hope that your friend taking the 
photo down would in fact delete the photo, but I'm sorry to say that isn't 
always the case.

Inspired by [Jacqui Cheng's article][1], I decided to test some of the 
more popular online services for photo hosting to see what happens when you
press the delete button on a photo from their site. On **November 
14<sup>th</sup>, 2009**, I uploaded and then deleted the following image of
a black box with white text to Facebook, Flickr, Picasa, MySpace, Photobucket, 
Shutterfly, Twitpic and WalMart. A few months later, 
I also added drop.io and Orkut: 

![I will attempt to delete this photo]({filename}/images/photo-deletion-tests/PostedAndDeleted.jpg)

When you look below, if you can see the black box for a site, 
that means that it was not truly deleted and is still live. You can verify 
this by clicking on the image. This is checked each time this page is 
loaded, so the information is constantly verified. If the image has been 
deleted, you will see the date that it was deleted.

There are a number of reasons why photo services might be lazy about 
properly removing images from their site, but until they have proper 
deletion mechanisms, we should all think twice about what we upload.

If there's a service that is not shown here that you'd like to see, 
please <a href="/contact">let me know</a>. And now, without further ado, 
I present, the ongoing results of the test:


## Facebook

Facebook properly deleted the photo from their server as of May 27, 2010.


## Flickr

Flickr began showing the following message approximately an hour after the 
image was deleted.

![Flickr Response]({filename}/images/photo-deletion-tests/flickr-response.jpg)


## Picasa

Picasa properly deleted the photo from their server as of at least November
15, 2009.


## MySpace

At an unknown time, MySpace began showing this photo instead:

![MySpace Response]({filename}/images/photo-deletion-tests/myspace.png)


## Photobucket

Photobucket properly deleted the photo from their server as of at least 
November 14, 2009.


## Shutterfly

As of 2014-08-22, Shutterfly still shows [the original image on their 
server][2].


## Twitpic

Twitpic properly deleted the photo from their server as of at least 
November 14, 2009.


## Walmart

As of 2014-08-22, Walmart still shows [the original image on their 
server][3].


## Google Orkut (added 2010-01-28)

Despite being [nearly shut down completely][4], as of 2014-08-22, 
Orkut still shows [the original image on their server][5].


## Drop.io (added 08 March 2010)

Drop.io properly deleted the photo from their server as of 8 March 2010, 
the day it was added.

[ftc]: http://www.ftc.gov/bcp/workshops/privacyroundtables/index.shtml
[1]: http://arstechnica.com/web/news/2009/07/are-those-photos-really-deleted-from-facebook-think-twice.ars
[2]: http://im1.shutterfly.com/media/47b9cf35b3127ccef8c9be9d18a800000040O00ActW7Ro4cuWQPbz4W/cC/f%3D0/ps%3D50/r%3D0/rx%3D720/ry%3D480/
[3]: http://images.photos1.walmart.com/232323232%7Ffp432%3B4%3Enu%3D3%3A%3A2%3E%3A8%3A%3E238%3EWSNRCG%3D326634885%3B329nu0mrj
[4]: http://thenextweb.com/google/2014/06/30/google-shutting-orkut-social-network-september-30/
[5]: http://images.orkut.com/orkut/photos/NwAAAA40TqrVmtf2vIA1oouDdb9vUTcjWDAQqVo_mBa45mvjdqMPiHhSaHxekFNT596b5sVYh593XRK-5Nquk0_WOQMAm1T1UJmPN1ZDUab24PgUE8b4ZMm09Mjj.jpg
