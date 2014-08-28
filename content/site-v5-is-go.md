Title: New Version of the Site is Now Live
Subtitle: Better, Faster, Stronger
Date: 2014-08-27
Tags: meta, blog, me
Categories: Tech

[TOC]

I have big news today for the small world of people who read my blog regularly:
A new version of the site is now live and the old version shall die a quick
death. 

Version 4 was pretty nice though, while it lasted:

![Site v4]({filename}/images/oldsite/v4.png)

*Other old versions of the site [still available][old]!*

## The improvements

This new version comes with some big improvements that I'm quite 
pleased with:

1. If you find typos in a blog post, you can edit them on Github and I can 
   easily integrate your changes. Check out the link on the right to 
   edit the typos in this very page. (I've left a few conspicuous ones as a 
   treasure hunt for the reader!)
1. The site is now *much* faster and can handle immense traffic without a 
   hitch, thanks to being hosted by [Github Pages][ghp]. The previous version would
   have occasional hiccups during times of high traffic &ndash; something that's 
   really quite untenable.
1. Comments are now moved to [Disqus][1], though unfortunately old comments have
   not made the jump to the new version of the blog. Comments are collapsed by 
   default so the scrollbar actually represents the length of a 
   highly-commented post.
1. The site now looks bad-ass. Regardless of whether you're on a phone, tablet
   computer, or what-have-you, it's going to look good.
1. All content has been categorized as well as tagged, as you can see in the 
   sidebar. There are Atom feeds for each.
1. The homepage has a new design that focuses on my projects and bio, and then 
   has recent posts below that.
1. Long articles like this one get an automatic table of contents on the 
   left.
1. The site is now optimized for speed dial in Opera and to be made into apps
   on mobile phones and tablets. For example, if you're reading this on 
   Android Chrome, you can simply click "Add to homescreen" in the `⋮`
   thing and you'll be all set.
1. Security is now invincible: No more webserver to update, no more database, 
   no more outdated Drupal. It's basically impossible to hack the new site. 
   I've also added my [PGP key][gpg] to the [contact page][c], for those 
   interested. 
1. The entire site is now static and doesn't require that I pay for or maintain
   a server or database. Bonus!

So those are the high-level changes you can see as of now. If you're interested
in the technical nitty-gritty, read on.

## The Tech

The original motivation to rebuild the site came when the old version kept 
overwhelming the server that was running it and requiring that I step in to 
make it work again. And if that weren't annoying enough, I have been paying
for that server for the past several years, which just seems a bit silly for
a simple blog like this one. 

The solution? A so-called [Static Site Generator][3] or SSG. With one of these,
the paradigm for your site totally changes. Instead of having a dynamic site
that loads every time somebody visits the page or makes a comment, you 
generate the *entire* website on your laptop (this takes about 30 seconds), 
creating static HTML, and then push that to some cloud provider of choice (in 
my case, I use Github pages for this because it's free and easy).

There are about 300 SSGs right now and the one I eventually landed on was 
[Pelican][4] due to it being written in a language I knew (Python), and due to
it having lots of good themes and plugins. I briefly tried to make a switch to
[Hugo][5] instead because it's written in Go and is much faster at generating 
content, but the documentation for Hugo isn't very good yet, and [it
doesn't support basic pagination][pagination], which is something of a showstopper. 


### Switching to a SSG from Drupal

Switching from Drupal was pretty awful and took a *lot* of effort &mdash; 
*days* of it! The goal was to get all of my posts exported from Drupal, 
convert them all to markdown, and to get them all live on Github pages. Let's 
go through this process together. 

### Exporting from Drupal

This step of the puzzle was, shall we say, a pain. Nobody has yet made a 
Drupal to Pelican converter, so I had to do it myself. [The script][6] that I 
wrote dug directly into Drupal's database, pulled out the contents
and converted them to a format that Hugo could understand. At the time I 
thought Hugo would be the SSG for me, but later I switched to Pelican, and had
to write [another script][7] to make the conversion from Hugo to Pelican.


### Problems with Drupal

This was a good start, but Drupal has a few funny conventions. One is that it
allows files to be "attached" to blog posts. Most blogs don't do this (Pelican
and Hugo included), so I had to go through all of the items that I attached to 
Drupal posts and convert them to inline links instead. This took a while.

Another problem I ran into is that the posts themselves were written directly 
in HTML, which makes them kind of awful, and not very portable between blog
engines. Content for Hugo or Pelican should be written in Markdown, so I began
making this conversion to the [200+ posts][9] on the site. In general, the process
for this was to find a post and begin cleaning it up. If I encountered 
something that a computer could reliably fix across all the posts (for example,
`<i>` can be converted to `*` and `<strong>` to `**`), I wrote a little script 
to do so. In the end, this took a lot of time, but I now have a collection of
a few hundred nicely-formed markdown files that power the blog.
 
### Moving to Github Pages

With all of the content converted properly, the remaining step was to get the
project live on Github. I found this process confusing, but the process is 
basically this:

1. You need to take the output file from Pelican and put it into a Git 
branch called `gh-pages`. To do this with Pelican is remarkably easy, as there is
a simple command you can run: `make github`. Run that, and you'll be all set,
with the content pushed and everything.

2. You need [a file named CNAME][cname] that simply contains the domain of your 
website. This is easy in theory -- it's just a plaintext file -- but in 
practice it is difficult because you need the file to be created by the 
`make github` command mentioned above. To do that add the CNAME file to a
directory at `content/extra/CNAME` and then add the following to your pelican
configuration file:

        :::python3
        EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
        STATIC_PATHS.append('extra/CNAME')

    Do that, and the file will get copied over whenever you run `make github`.
    
    If you've done this correctly, you'll see evidence of such in the 
    repository's settings page on Github, where it will tell you the domain
    in the CNAME.

3. You need to configure your DNS provider to point your domain to Github.
This varies by provider, but I can tell you that your final version should
look something like this:

        :::txt
        ↪ dig www.michaeljaylissner.com +nostats +nocomments +nocmd
        
        ; <<>> DiG 9.9.5-3-Ubuntu <<>> www.michaeljaylissner.com +nostats +nocomments +nocmd
        ;; global options: +cmd
        ;www.michaeljaylissner.com.	IN	A
        www.michaeljaylissner.com. 3600	IN	CNAME	mlissner.github.io.
        mlissner.github.io.	3600	IN	CNAME	github.map.fastly.net.
        github.map.fastly.net.	2	IN	A	199.27.79.133
        fastly.net.		66087	IN	NS	ns4.p04.dynect.net.
        fastly.net.		66087	IN	NS	ns3.p04.dynect.net.
        fastly.net.		66087	IN	NS	ns2.p04.dynect.net.
        fastly.net.		66087	IN	NS	ns1.p04.dynect.net.


## Final Words

This is been a much larger undertaking than I expected, with tons of corner
cases that I wanted to fix before releasing a new version of the site. In the 
end though, this has been a good investment that I can expect to keep the site
going for the next five to ten years.

I hope you enjoy the new look and new features.


[1]: https://disqus.com
[3]: http://staticsitegenerators.net/
[4]: https://github.com/getpelican/pelican/
[5]: http://hugo.spf13.com/
[6]: {filename}/scripts/drupal_to_hugo.py 
[7]: {filename}/scripts/convert_from_hugo_to_pelican.py
[ghp]: https://pages.github.com/
[gpg]: {filename}/archive/mike.gpg
[c]: {filename}/pages/contact.md
[pagination]: https://github.com/spf13/hugo/issues/96
[9]: /archives.html
[cname]: https://github.com/mlissner/michaeljaylissner.com/blob/gh-pages/CNAME
[old]: {filename}/pages/about.md
