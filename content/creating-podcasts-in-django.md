Title: Creating Podcasts in Django
Subtitle: It's more work than you'd think
Summary: You'd think that creating podcasts would be fairly easy, but surprisingly the documentation is overly long and the tools are overly complex. Herein, I discuss solutions to these issues and a generalized approach to making and hosting a podcast in your Django app. 
Date: 2014-09-15
Status: Draft
Tags: podcast, CourtListener, django
Category: Tech

[TOC]

Podcasts were [created about a decade ago][wikipedia] as a way for creators of audio and video content to share their work freely in a way that fans of a show could easily use to get updates whenever a new episode was created. Over the past decade, thousands of podcasts have been created (the current estimate is [115,000 English podcasts][count]), but oddly, the tooling for podcast hosts such as myself remains fairly poor. After trawling the Internet and building podcast support into [CourtListener][cl], I've come up with [a few tools][tools], and I've written up some notes for an easy way to create podcasts in Django. 


## Making a Podcast with Django

There are currently two apps designed to make podcasting in Django easy, [django-podcast][podcast] and its successor of sorts, [Django Podcasting][podcasting]. I dug into the code of both of these, but from my perspective, they both offer too much and this is a case where less is more. How hard, I ask you, is it to create an XML file linking to some MP3 files? Not that hard.

### Making XML Files

The process here is to dig into the 


## Testing your podcast locally and with a validator


## Including your podcast in the iTunes library


## Validating that everything works

1. Check validator XXX
1. Check iTunes/Rhythmbox 


## Tools and References

1. Somewhat surprisingly, [the most definitive documentation for podcasts][docs] comes from Apple rather than a standards body. This document is the best description of the requirements for Podcasts that I have found.
1. The best podcast validator I have found is [this one][validator].
1. [Django's syndication framework][syndication]



An image:

![Alt Text]({filename}/images/han.jpg)

Some links:
[a link relative to content root]({filename}/article1.md)
[a link relative to current file]({filename}../article1.md)


[wikipedia]: https://en.wikipedia.org/wiki/Podcast
[docs]: https://www.apple.com/itunes/podcasts/specs.html
[rsspec]: http://www.rssboard.org/rss-specification
[atomspec]: https://tools.ietf.org/html/rfc4287
[validator]: XXXXX
[count]: http://themyndset.com/2012/01/how-many-podcasts-are-there-whats-the-future-of-the-podcast/
[tools]: #tools-and-references
[cl]: https://www.courtlistener.com
[podcasting]: https://github.com/rizumu/django-podcasting
[podcast]: https://github.com/jefftriplett/django-podcast
[syndication: https://docs.djangoproject.com/en/dev/ref/contrib/syndication/
