Title: Calculating the average elevation of a trip using a TCX file
Date: 2012-09-16T10:33:31
Tags: ridewithgps, hiking, hacking, GPS, elevation, biking
Category: Tech


If you use a site like [ridewithgps][1], something you may want to know is how to calculate the average elevation for a trip. Unfortunately, most sites don't seem to provide this, so we have to do a little hacking. 

Here's what worked for me:

 - download the GPS TCX file
 - grep out the altitude lines (`grep -i 'altitude' your_file.tcx`)
 - find & replace out the remaining XML tags and whitespace using a basic text editor
 - average the remaining values in a spreadsheet

Takes about five minutes. For [my trip][2] the number came out to be 10,753 feet!

[1]: http://ridewithgps.com
[2]: http://ridewithgps.com/routes/1701701
