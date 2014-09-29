Title: Updating Bulk Data in CourtListener
Subtitle: Bulk Data Can Be Hard
Summary: There's a beautiful and growing trend towards bulk data, but in this post I discuss the challenges we have at CourtListener and some solutions we've developed. 
Date: 2014-09-28
Tags: bulk data, courtlistener.com
Categories: Tech

[TOC]

There's an increasing demand for bulk data from government systems, and while this will generate big wins for transparency, accountability, and innovation (at the occasional cost of privacy[^privacy]), it's important to consider a handful of technical difficulties that *can* come along with creating and providing such data. Do *not* misread this post as me saying, "bulk data is hard, don't bother doing it." Rather, like most of my posts, read this as an in-the-trenches account of issues we've encountered and solutions we've developed at CourtListener. 


## The Past and Present

For the past several years we've had [bulk data at CourtListener][1], but to be frank, it's been pretty terrible in a lot of ways. Probably the biggest issue with it was that we created it as a single massive XML file (~13GB, compressed!). That made a lot of sense for our backend processing, but people consuming the bulk data complained that it crashed 32 bit systems[^sympathy], consumed memory endlessly, decompressing it wasn't possible on Windows[^sympathy], etc. 

On top of these issues for people consuming our bulk data, and even though we set it up to be efficient for our servers, we did a stupid thing when we set it up and made it so our users could generate bulk files whenever they wanted for any day, month, year or jurisdiction. And create bulk files they did. Indeed in the year since we started keeping tabs on this, people made nearly fifty thousand requests for time-based bulk data[^stats]. 

On the backend, the way this worked was that the first time somebody wanted a bulk file, they requested it, we generated it, and then we served it. The second time somebody requested that same file, we just served the one we generated  before, creating a disk-based cache of sorts. This actually worked pretty well but it let people start long-running processes on our server that could degrade the performance of the front end. It wasn't great, but it was a simple way to serve time- and jurisdiction-based files.[^file-count] 

As any seasoned developer knows, the next problem with such a system would be cache invalidation. How would we know that a cached bulk file had bad data and how would we delete it if necessary? Turns out this wasn't so hard, but every time we changed (or deleted) an item in our database we had code that went out to the cache on disk and deleted any bulk files that might contain stale data. Our data doesn't change often, so for the most part this worked, but it's the kind of spaghetti code you want to avoid. Touching disk whenever an item is updated? Not so good.  

And there were bugs. [Weird ones][date-bug].
   
Yeah, the old system kind of sucked. The last few days I've been busy re-working our bulk data system to make it more reliable, easier to use and just overall, better.


## The New System

Let's get the bad news taken care of off the bat: The new system no longer allows date-based bulk files. Since these could cause performance issues on the front end, and since [nobody opposed the change][list], we've done away with this feature. It had a good life, may it RIP.

The good news is that by getting rid of the date-based bulk files, we've been able to eliminate a metric *ton* of complexity, [literally][define-literal]! No longer do we need the disk-cache. No longer do we need to parse URLs and generate bulk data on the fly. No longer is the code a mess of decision trees based on cache state and user requests. Ah, it feels so free at last! 
 
And it gets even better. On top of this, we were able to resolve [a long-standing feature request][2] for complete bulk data files by jurisdiction. We were able to make the schema of the bulk files match that of [our REST API][rest-api]. We were able to make the bulk file a tar of smaller JSON files, so no more issues unzipping massive files or having 32 bit systems crash. [We settled all the family business][godfather].

Oh, and one more thing: When this goes live, we'll have bulk files and an API for oral arguments as well -- Another CourtListener first. 
 

## Jeez, That's Great, Why'd You Wait So Long?
 
This is a fair question. If it was possible to gain so much so quickly, why didn't we do it sooner? Well, there are a number of reasons, but at the core, like so many things, it's because nothing is actually that easy. 

Before we could make these improvements, we needed to: 

 - Make sure the impact on our users [wouldn't be an issue][list]
 - Test the performance of generating more than 350 bulk files at the end of each month[^dev-aside]
 - Have [our REST API][rest-api] in place so we could use it to generate the bulk files
 - Complete [performance profiling][profiling] to identify [hot spots][hotspots] in the new bulk data API
 - [Rewrite the documentation][docs]

And pretty much everything else you can imagine. So, I suppose the answer is: We waited so long because it was hard. 

But being hard is one thing. Another thing is that although a number of organizations have used our bulk data, never has any contributed either energy or resources to fixing the bugs that they reported. Despite the benefits these organizations got from the bulk files, none chose to support the ecosystem from which they benefited. You can imagine how this isn't particularly motivational for us, but we're hopeful that with the new and improved system, those using our data will appreciate the quality of the bulk data and consider [supporting us][donate] down the road.  

## Wrapping Up

So, without sucking on too many sour grapes, that's the story behind the upgrades we're making to the bulk files at CourtListener. At first blush it may seem like a fairly straightforward feature to get in place (and remember, in *many* cases bulk data is stupid-easy to do), but we thought it would be interesting to share our experiences so others might compare notes. If you're a consumer of CourtListener bulk data, we'll be taking the wraps off of these new features soon, so make sure to watch the [Free Law Project blog][flp]. If you're a developer that's interested in this kind of thing, we're eager to hear your feedback and any thoughts you might have. 



[1]: https://www.courtlistener.com/api/bulk-info/
[taxis]: https://medium.com/@vijayp/of-taxis-and-rainbows-f6bc289679a1
[date-bug]: https://github.com/freelawproject/courtlistener/issues/278
[list]: http://lists.freelawproject.org/pipermail/dev/2014-August/000069.html
[2]: https://github.com/freelawproject/courtlistener/issues/285
[rest-api]: https://www.courtlistener.com/api/rest-info/
[godfather]: https://www.youtube.com/watch?v=8vZx7yF_a7M
[profiling]: https://github.com/freelawproject/courtlistener/commit/a0e4326d98e9f501ec3e69955d6b5650471686e8#diff-30d04f22c69dda9704be56ec95d9d2c1R68
[hotspots]: https://github.com/freelawproject/courtlistener/commit/a0e4326d98e9f501ec3e69955d6b5650471686e8#diff-6f850cf75fe2e1d17284e0b701b26b06L47
[docs]: https://github.com/freelawproject/courtlistener/commit/52e8eff985fdf75612837cef4d9ef55ad60f29ad#diff-6
[define-literal]: http://theweek.com/article/index/241002/how-the-wrong-definition-of-literally-snuck-into-the-dictionary
[donate]: https://www.courtlistener.com/donate/
[^privacy]: For example, a few days ago some folks got access to NYC taxi information in bulk. In theory it was anonymized using MD5 hashing, but because there were a limited number of inputs into the hashing algorithm, all it took to de-anonymize the data was to compute every possible hash ("[computing the 22M hashes took less than 2 minutes][taxis]") and then work backwards from there to the original IDs. While one researcher did that, another one began finding images of celebrities in taxis and figuring out where they went. Privacy is hard.
[^sympathy]: I confess I'm not *that* sympathetic...
[^stats]: To be exact: 48271 requests, as gathered by our stats module.
[^file-count]: 
    So far, 17866 files were created this way that haven't been invalidated, as counted by: 

        find -maxdepth 1 -type d | while read -r dir; do printf "%s:\t" "$dir"; find "$dir" -type f | wc -l; done
[^dev-aside]: 
    Commence a fun digression for the developers. As you might expect, aside from compressing bulk files, the bottleneck of generating 350+ bulk files at once is pulling items from the database and converting them to JSON. We tried a few solutions to this problem, but the best we came up with takes advantage of the fact that every item in the database belongs in exactly two bulk files: The all.tar.gz file and the {jurisdiction}.tar.gz file. One way to put the item into both places would be to generate the all.tar.gz file and then generate each of the 350 smaller files. 
    
    That would iterate every item in the database twice, but while making the jurisdiction files you'd have to do a lot of database filtering...something that it's generally good to avoid. Our solution to this problem is to create a dictionary of open file handles and then to iterate the entire database once. For each item in the database, add it to both the all.tar.gz file and add it to the {jurisdiction}.tar.gz file. Once complete, close all the file handles. For example:
        
        :::python
        # Get all the courts
        courts = Court.objects.all()
        
        # Create a dictionary with one key per jurisdiction
        tar_files = {}
        for court in courts:
            tar_files[court.pk] = tarfile.open(
                '/tmp/bulk/opinions/%s.tar.gz' % court.pk,
                mode='w:gz',
                compresslevel=1,
            )
        
        # Then iterate over everything, adding it to the correct key
        for item in item_list:
            # Add the json str to the two tarballs
            tarinfo = tarfile.TarInfo("%s.json" % item.pk)
            
            tar_files[item.docket.court_id].addfile(
                tarinfo, StringIO.StringIO(json_str))
            tar_files['all'].addfile(
                tarinfo, StringIO.StringIO(json_str))
        
    In a sense the first part creates a variable for every jurisdiction on the fly and the second part uses that variable as a dumping point for each item as it iterates over them. 
    
    A fine hack.

[flp]: http://freelawproject.org
