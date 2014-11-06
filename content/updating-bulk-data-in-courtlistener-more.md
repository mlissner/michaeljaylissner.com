Title: Updating Bulk Data in CourtListener...Again
Subtitle: Can You Do it Faster?
Summary: I wrote a few weeks ago about our wonderful new bulk data system. It's great, but not fast enough. Now it is.
Date: 11/6/2014
Tags: Bulk Data, CourtListener
Category: Tech

I [wrote a few weeks ago][old] about our new system for creating [bulk files in CourtListener][cl]. The system was pretty good. The goal was and is to efficiently create one bulk file for every jurisdiction--object pair in the system. So, that means one bulk file for oral arguments from Supreme Court, another for opinions from the Ninth Circuit of Appeals, another for dockets from Alabama's appellate court, etc. We have about 350 jurisdictions and four different object types right now, for a total of about 1,400 bulk files.

This system needs to be fast.
   
The old system that I wrote about before would create 350 open file handles at a time, and then would iterate over each item in the database, adding it to the correct file as it inspected the item. This was a beautiful system because it only had to iterate over the database once, but even after [performance tuning][tuner], it still took about 24 hours. Not good enough. 

I got to thinking that it was terrible to create the entire bulk archive over and over when in reality only a few items change each day. So I created a [bug to make bulk data creation incremental][inc]. 

This post is about that process.


## The First Approach

The obvious way to do this kind of thing is to grab the bulk files you already have (as gz-compressed tar files), and add the updated items to those files. Well, I wrote up code for this, tested it pretty thoroughly and considered it done. Only to realize that, like regular files, when you create a compressed tar file with a command like this...   

    :::python
    tar_files['all'] = tarfile.open('all.tar.gz', mode='w:gz')
    
...it clobbers any old files that might have the same name. So much for that.
  

## Next Approach

Well, it looked like we needed append mode for compressed tar files, but alas, from [the documentation][pydocs]:

> Note that 'a:gz', 'a:bz2' or 'a:xz' is not possible.
 
"a:gz" means a gz-compressed tar file in **a**ppend mode, so much for that idea. Next! 


## Next Approach

Well, you can't make gz-compressed tar files in append mode, but you can create tar files in append mode as step one, then compress them as step two. I tried this next, and again, it looked like it was working...until I realized that my tar files contained copy after copy after copy of each file. I was hoping that it'd simply clobber files that were previously in the file, but instead it was just putting multiple files of the same name into the tar. 

Perhaps I can delete from the tar file before adding items back to it? [Nope, that's not possible either][del]. Next idea?


## Final Approach

I was feeling pretty frustrated by now, but there was one more approach, and that was to add an intermediate step. Instead of creating the tar files directly in Python, I could save the individual `json` files I was previously putting into the tar file to disk, then create the compressed tar files directly from those once they're all created. We proved earlier that Python has no issues about clobbering items on disk, so that'll work nicely for incremental bulk files, which will just clobber old versions of the files.
 
From performance analyses of the code, most of the bottleneck is in serializing JSON, so this will change it so that gets done at most once per item in the database and then most of the remaining work will be making tar files and gz-compressing them. 

## Whew!

I was hoping that I would be able to easily update items inside a compressed tar file, or even inside an uncompressed tar file, but that doesn't seem possible. 

I was hoping that I could create these files while iterating over the database, as described in the first approach, but that's not doable either. 

At the end of the day, the final method is just to write things to disk. Simple beats complicated this time, even when it comes to performance. 


[old]: {filename}/updating-bulk-data-in-courtlistener.md
[cl]: https://www.courtlistener.com/api/bulk-info/
[tuner]: https://github.com/freelawproject/courtlistener/commit/a0e4326d98e9f501ec3e69955d6b5650471686e8
[inc]: https://github.com/freelawproject/courtlistener/issues/293
[pydocs]: https://docs.python.org/3/library/tarfile.html
[del]: http://bytes.com/topic/python/answers/40408-deleting-tarfile
