Title: Pacific Crest Temperature Project
Subtitle: Alas, now defunct!
Date: 2007-11-21
Tags: java, pct, programming
Categories: Backpacking
Menu: False

[TOC]

## Introduction
As mentioned in a [previous blog post][1], in 2005 and 2006 six hikers carried 
[iButton thermocron][2] devices 2,650 miles from Mexico to Canada along the 
[Pacific Crest Trail][3]. These devices consist of a sealed canister about the
size of five stacked dimes. Inside the canister is the following:

 - A piece of computer memory
 - A digital clock
 - A thermometer
 
Each hour, these devices were programmed to check the temperature and record 
it to the memory. Upon returning from the journey, the devices were connected 
to a computer and the data was extracted. All told, there are about 18,522 
data points &ndash; too many to be plotted in any one graph. As a result of 
the struggle to make meaningful use of this data, the applet below was created. 


## Applet and Java Project

This applet was created as a final project for Java: Discovering its Power, a 
class offered by [University of California Berkeley Extension][4]. The source 
code is [on github][5], and modifications or updates are more than 
welcome. You can find the hiker's raw data in the [data directory][6]. You 
will see that it is in `.csv` format. The fields are: month, day, year, hour, 
temperature).

To use the applet, simply select the date range that you are interested in 
displaying, the time of day that interests you, the hikers whose data you want 
to see, and press the 'generate' button.

## Caveats and Warnings

There are a few caveats about using this data:

 - The primary caveat is that these results are all passive data, which is to 
 say that these measurements were not taken by a careful experiment, but 
 rather by a device that was carried somewhere in a backpack for the length of 
 a five month journey. As a result, the figures shown can vary greatly 
 depending on how the device was treated, where it was when it took its 
 measurement, and any number of other factors.
 - Ground temperatures and solar energy can be very extreme. Many of these 
 hikers carried their iButton in a pack that might have been set within one or 
 two inches of the ground or directly in the sun, where the temperature can 
 seem unreal. I have seen measurements ranging from about 10 to 160 degrees F. 
 These are actual measurements.
 - Different hikers move at different paces, and take off-trail days at 
 different times. There is no guarantee that the figures you are looking at 
 were measured while the hiker was on the trail.


## Hiker Start and End Dates

Adam Bradley: 5/15/06 to 9/24/06  
Matt Church: 4/28/06 to 6/22/06  
Robert Francisco: 4/25/06 to 9/26/06  
Michael Lissner: 4/21/05 to 9/12/05  
Jeff Singewald: 4/22/06 to 9/6/06  


## The Applet

Unfortunately, the applet has been retired due to the obviation of Java 
Applets. Try though I might to make it continue working, ultimately it needs to
be recoded, likely in JavaScript. Contributions welcome.

## Bugs and Questions

Inevitably, we shall find bugs and problems with this applet. When that 
happens, please post them on Github.

Any questions about the use of this applet are more than welcome. Just [send 
me a jot][7] or make a comment below.

[1]: {filename}/great-temperature-data-project.md
[2]: http://www.maxim-ic.com/products/ibutton/
[3]: http://www.pcta.org
[4]: http://www.unex.berkeley.edu/
[5]: https://github.com/mlissner/pct-temperature-project/
[6]: https://github.com/mlissner/pct-temperature-project/tree/master/data
[7]: {filename}/pages/contact.md
