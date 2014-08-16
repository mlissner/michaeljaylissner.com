Title: Announcing CourtListener.com
Date: 2010-05-01T20:08:16
Tags: Final Project, courtlistener.com, announcements


I'm elated to announce today that I am officially taking the ropes of my final project and letting it loose into the wild. It's been seven months since development on it officially started and finally, the beta version is done. 

If you haven't been following along, the <a href="http://courtlistener.com">project itself</a> is an open source legal research tool which allows anybody to keep up to date with federal precedents as they are set by the 13 Federal Circuit courts. Right now, it has <a href="http://courtlistener.com/coverage/">more than 130,000 documents in its corpus</a>, including almost all of the Supreme Court record dating back to 1754. Every day it downloads the latest documents within about a half hour of when each court publishes them.

One thing we've focused on while building the site has making it as useful as possible for as many people as possible. Since not everybody likes getting updates in their inbox, we've also tied the search engine in with an Atom feed generator so that you can search for whatever you want, and then follow updates in your feed reader.

Everything we've built uses a powerful boolean search engine on the backend. At present, there are <a href="http://courtlistener.com/search/advanced-techniques/">a ton of boolean connectors</a> that you can use on our site to search our corpus or create alerts and feeds. Unlike full text search that most people are familiar with, boolean search allows incredibly complex queries, such as every document mentioning Attorney General Holder that is published in the Third Circuit of Appeals (<a href="http://courtlistener.com/search/results/?q=%40court+ca3+%40doctext+holder&search=">@court ca3 @doctext holder</a>), or perhaps every document that mentions "Roe" and "Wade" within ten words of each other (<a href="http://courtlistener.com/search/results/?q=%40doctext+%22roe+wade%22~10&search=">@doctext "roe wade"~10</a>).

But that's not all. Because we also want you to be able to use this efficiently during your day-to-day searching, we've built an <a href="http://courtlistener.com/tools/">add-on that will work in most browsers</a>, which allows you to search CourtListener.com without first going to our homepage.

You can also browse all of documents in our corpus, or you can go to the details page for an opinion, where you can read the text of its body without having to download a PDF and crank up Adobe Acrobat.

As I mentioned earlier, this project has been designed as an open source project, so if you're looking for something to contribute to, look no further. We have a very active <a href="http://bitbucket.org/mlissner/legal-current-awareness/issues?status=new&status=open">bug list</a> where you can dip your toes in, or if you prefer something meatier, we can cook something up specifically for you.

I've greatly enjoyed working on this project so far, and I'd love to get more people using it, working on it, and recommending it to their friends. We're already planning version 1.0, so drop me a line if you're interested in helping out, otherwise, <a href="http://courtlistener.com">go check it out already</a>, and see all that it has to offer!