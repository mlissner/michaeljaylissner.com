#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mike Lissner'
SITENAME = 'Michael Jay Lissner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 30
DEFAULT_ORPHANS = 2

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = True
SLUGIFY_SOURCE = 'basename'
DELETE_OUTPUT_DIRECTORY = True

# Sadly disabled because it wraps capital letters in HTML attributes in still
# more HTML. Possible to toggle and verify by looking at "Previous" link at:
# https://mlissner.github.io/michaeljaylissner.com/posts/2013/07/19/battery-packs-for-ultralight-long-distance-backpacking/
TYPOGRIFY = False

# URL settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

TAG_FEED_ATOM = 'feeds/tag/%s'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'sitemap',
    'tipue_search',
    'extract_toc',
]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.4,
        'pages': 0.6
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Elegant theme settings
THEME = "elegant"
RECENT_ARTICLES_COUNT = 20
COMMENTS_INTRO = "I love getting feedback and comments. Make my day by making " \
                 "a comment."
SITE_LICENSE = 'Unless mentioned otherwise, all material on this site is ' \
               '<a href="about#license">licensed</a> under a Creative ' \
               'Commons copyright or the GNU Affero GPL. ' \
               '<a href="about#privacy">Privacy Policy</a>.'
MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra', 'headerid',
                  'toc'])
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     '404'))
STATIC_PATHS = ['theme/images', 'images', 'archive', 'pdfs']
ARTICLE_EXCLUDES = ['archive', 'pdfs']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHOR = "Michael Lissner"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME = 'michaeljaylissner'
