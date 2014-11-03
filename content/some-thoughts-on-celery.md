Title: Some Thoughts on Celery
Subtitle: A love-hate relationship
Summary: Celery drives me nuts. Celery allows background tasks. I hate Celery. I love Celery.
Date: 11/1/2014
Tags: Celery, Python, Rant 
Category: Tech
Status: Draft


We finally upgraded [CourtListener][cl] last week and things went pretty well with the exception of two issues. First, we had some extended downtime as we waited for the database migration to complete. In retrospect, I should have realized that updating every item one row at a time would take a while. My bad. 

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
    
2. No log messages...*anywhere*. this must have something to do with daemonizing things, but no matter what I did I couldn't find any log messages anywhere.
 
3. The collection of things that happens when `celery` starts is complicated:

    1. I call `sudo service celeryd start`
    1. `service` calls `/etc/init.d/celeryd`
    1. `celeryd` does some stuff and calls `celery.sh` (another file altogether), where my settings are.
    1. Control is returned to `celery`, which starts celery itself with a command generated from `celery.sh`.
    
    On top of this, there's a `celery` binary and a celery [management command][dj-man] for Django. `celery --help` prints out 68 lines of documentation. Not too bad, but many of those lines refer you to other areas of the documentation. For example, `celery worker --help` prints another 100 lines of help text. *Jesus* this thing is complicated. 
    
    Did I mention it has [changing APIs][apis]?
    
I digress a bit, but the point here is that it fails silently, there are no log messages when it fails, and there's no way to know which part of a complicated infrastructure is the problem. End rant.[^1]


## Seeking Sanity

It took me a long time to figure out what was going wrong, but I did eventually figure it out. The process, in case you run into something similar, is to modify `celeryd` so it prints out the command that it eventually runs. At that point you'll have the correct command. With that, you can run it as the `celery` user and with some luck you'll see what the problem is. There's [a modified init script for this purpose, if you like][dry].
 
Other tips:

1. If you have a new enough version of Celery, there are [some troubleshooting tips][trouble] that should help. They did nothing for me, because I haven't upgraded yet for fear of the changing APIs.

2. There seem to be a handful of different command line flags that Celery can use to be sent to the background. You'll need to disable these when you're testing or else you won't see error messages or anything (apparently?).


## Moving Forward

So, I feel bad: I've ranted a good deal about Celery, but I haven't proposed any solutions. What would it take to make Celery a less complicated, more reliable tool? 

The ideas I've come up with so far are: 

 - More documentation for installation and set up troubleshooting with the possibility of a wiki.
    - But already I rant about how much documentation it has.
 - A simpler interface that eliminates a number of edge usages.
    - But I have no idea what, if anything, can be eliminated. 
 - Support for fewer task brokers.
    - But I use RabbitMQ and am considering switching to Redis.
 - A more verbose, more thorough debug mode.
    - But apparently this is already in place in the latest versions?
 - Let Celery run as the `www-data` user?
    - But apparently that's a bad idea.
   
As you can tell, I don't feel strongly that any of these are the right solution. I am convinced though that Celery has a bad smell and that it's ripe for a leaner solution to fill some of its use cases. I'm currently considering switching to a simpler task queue, but I don't know that I'll do it since Celery is the de-facto one for Django projects.

We deserve a good, simple, reliable task queue though, and I wonder if there are good ideas for what could be changed in Celery to make that possible.  


[^1]: In truth Celery is a classic love/hate relationship. On the one hand, it evokes posts like this one, but on the other, it allows me to send tasks to a background queue and distribute loads among many servers. Hell, it's good enough for Instagram. On the other hand, god damn it, when it fails I go nuts.

[1]: http://www.celeryproject.org/
[flp-oa]: http://freelawproject.org/2014/10/31/announcing-oral-arguments-on-courtlistener-2/
[dj-man]: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
[apis]: http://seeknuance.com/2012/07/30/celery-api-changes-drive-me-nuts/
[dry]: http://stackoverflow.com/a/21883578/64911
[trouble]: http://celery.readthedocs.org/en/latest/tutorials/daemonizing.html#troubleshooting
[cl]: https://www.courtlistener.com
