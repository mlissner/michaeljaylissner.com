Title: Some Thoughts on Celery
Subtitle: Postmortem on our upgrade and details on our love-hate relationship
Summary: Celery drives me nuts. Celery allows background tasks. I hate celery. I love celery.
Date: 11/1/2014
Tags: Celery, Python, Rant 
Category: Tech

[TOC]

We finally upgraded CourtListener last week and things went pretty well with the exception of two things. First, we had some extended downtime as we waited for the database migration to complete. In retrospect, I should have realized that updating every item one row at a time would take a while. My bad. 

Second, [Celery][1] broke again and that took me the better part of a day to detect and fix. As a central part of our infrastructure, this is really, *truly* frustrating. The remainder of this post goes into what happened, why it happened and how I finally managed to fix it. 


## Why?

First, why did this happen? Well...because I decided to log something. I created a task that processes [our new audio files][flp-oa] and I thought, "Hey, these should really log to the Juriscraper log rather than the usual celery log." So, I added two lines to the file: One importing the log file and the second writing a log message. *This* is the little change that brought Celery to a grinding halt. 


## What the Hell? 

If you're wondering why logging would break an entire system, well, the answer is because Celery runs as a different user than everything else. In our case, as the `celery` user -- a user that didn't have permission to the log file I requested. Ugh. 

Fine, that's not so bad, but there were a number of other frustrating things that made this much worse:
 
1. The Celery init script that we use was reporting the following:
    
        ↪ sudo service celeryd start
        celeryd-multi v3.0.13 (Chiastic Slide)
        > Starting nodes...
            > w1.courtlistener.com: OK

    But no, it was not starting "OK". It was immediately crashing.
    
2. No log messages...*anywhere*. this must have something to do with daemonizing things, but no matter what I did I couldn't find any log messages anywhere. Celery was reporting that everything was starting OK, with no errors *anywhere*, damn it.
 
3. The collection of things that happens when `celery` starts is complicated:

    1. I call `sudo service celeryd start`
    1. `service` calls `/etc/init.d/celeryd`
    1. `celeryd` does some stuff and calls `celery.sh` (another file altogether), where my settings are.
    1. Control is returned to `celery`, which starts celery itself with a command generated from `celery.sh`.
    
    On top of this, there's a `celery` binary and a celery [management command][dj-man] for Django. `celery --help` prints out 68 lines of documentation. Not too bad, but many of those lines refer you to other areas of the documentation. For example, `celery worker --help` prints another 100 lines of help text. *Jesus* this thing is complicated. 
    
    Did I mention it has [changing APIs][apis]?
    
I digress a bit, but the point here is that it fails silently, there are no log messages when it fails, and there's no way to know which part of a complicated infrastructure is the problem.


## Seeking Sanity

It took me a long time to figure out what was going wrong, but I did eventually figure it out. The process, in case you run into something similar, is to modify `celeryd` so it prints out the command that it eventually runs. At that point you'll have the correct command. With that, you can run it as the `celery` user and with some luck you'll see what the problem is. There's [a modified init script for this purpose, if you like][dry].
 
Other tips:

1. If you have a new enough version of Celery, there are [some troubleshooting tips][trouble] that should help. They did nothing for me, because I haven't upgraded due to the changing APIs.

2. There seem to be a handful of different ways that Celery can be sent to the background. You'll need to disable these when you're testing or else you won't see error messages or anything (apparently?).



[1]: http://www.celeryproject.org/
[flp-oa]: http://freelawproject.org/2014/10/31/announcing-oral-arguments-on-courtlistener-2/
[dj-man]: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
[apis]: http://seeknuance.com/2012/07/30/celery-api-changes-drive-me-nuts/
[dry]: http://stackoverflow.com/a/21883578/64911
[trouble]: http://celery.readthedocs.org/en/latest/tutorials/daemonizing.html#troubleshooting
