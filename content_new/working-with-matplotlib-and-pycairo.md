Title: Working with matplotlib and pycairo
Date: 2009-01-19T16:25:32
Tags: Python, programming, matplotlib, pycairo, project


I spent a good part of my winter break working on learning <a href="http://python.org" target="_blank">Python</a> and using it for projects. One project was the <a href="http://michaeljaylissner.com/blog/yelp-scraper" target="_blank">Yelp scraper</a> that I posted about previously, and another was a report for my old work. 

The report is a statistical analysis of the development of about 2,000 children aged three and four. For those interested, I'll try to post it here once the final version is ready to go. In the past when making the report, I had been frustrated because there was no easy way to script the creation of the 30 or so charts that need to be made. Excel had been our data analysis tool, and as such, we were stuck with either using VBA to create charts, or to do it by hand. Since nobody knew VBA, we always just buckled down and did the work by hand.

This time around, I discovered the <a href="http://matplotlib.sourceforge.net/" target="_blank">matplotlib Python library</a>, and used that to create the charts. It was an pretty rough experience all in all. While simple graphs can be created in about five lines of code, creating complicated ones took a good amount of work. For example, to change the tick markers on a graph requires that you create tick objects, and then manipulate them each individually in a for loop. Granted, I couldn't customize them at all in Excel, but figuring out that kind of change was a pain indeed. 

The report itself required about 1,000 lines of code, and each chart required about 100-200 lines. For custom charts, I didn't find the library that useful, however towards the end of the report there are 30 charts, all of which are identical, except for the data. For these charts, I was able to make a for loop that created them all in about 20 minutes, whereas previously these took me a few hours to make by hand. 

Another library I spent some time learning was the <a href="http://www.cairographics.org/pycairo/" target="_blank">pycairo</a> library, which allows pixel by pixel editing of pictures. I had planned to use it to do any editing to the charts that I was unable to accomplish with the matplotlib library, but in the end, it was unnecessary. I have another project coming up though that will use the pycairo library, so look for that soon.