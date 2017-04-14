# Here Lives Mike Lissner's Personal Website

This repo contains the blog posts, pages, and other junk associated with my 
website. If you're interested in fixing a typo or doing other such things, 
you're absolutely welcome to.


# Documentation of Common Tasks

## Updating the plugins and themes

Plugins and themes are in ../pelican-plugins and ../pelican-themes. You can 
update them individually by, changing into their directory, then:

    git pull --recurse-submodules
    git submodule update --recursive

That'll get and update the correct submodules.


## Updating the core requirements
 
You'll want to update Pelican from time to time. You can check your current
version with:

    pelican --version
    
If it's older than you want, you can update everything with:

    pip install -r requirements.txt --upgrade
    
And you'll then want to freeze the new requirements with:

    pip freeze > requirements.txt
    
    
## Running in debug mode

Easy, peasy, use the --verbose and --debug flags:

    pelican content -s pelicanconf.py --verbose --debug
    
    
## Prepping and pushing a release

To do this, go into the home directory for the blog and run:

    workon mjl.com
    make github

This will generate a release, put it in the `gh-pages` branch, and then push it
to Github.

Generally, after this is complete, a commit should be pushed to master with the
changes.


## Generating a specific page

This took some effort to figure out:

    pelican -s pelicanconf.py --write-selected output/posts/2014/10/14/becoming-a-non-profit/index.html --debug
