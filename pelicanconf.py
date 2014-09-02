#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mike Lissner'
SITENAME = 'Michael Jay Lissner'
SITEURL = '//localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 30
DEFAULT_ORPHANS = 2

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = True
SLUGIFY_SOURCE = 'basename'
DELETE_OUTPUT_DIRECTORY = True

TYPOGRIFY = True

# URL settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
    'sitemap',
    'tipue_search',
    'extract_toc',
    'neighbors',
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
THEME = "../pelican-elegant"
RECENT_ARTICLES_COUNT = 20
COMMENTS_INTRO = "I love getting feedback and comments. Make my day by making " \
                 "a comment."
SITE_LICENSE = 'Unless mentioned otherwise, all material on this site is ' \
               '<a href="about#license">licensed</a> under a Creative ' \
               'Commons copyright or the GNU Affero GPL. ' \
               '<a href="about#privacy">Privacy Policy</a>.'
MD_EXTENSIONS = ([
    'codehilite(css_class=highlight)',
    'extra',
    'headerid',
    'toc'
])

#MAILCHIMP
MAILCHIMP_FORM_ACTION = '//asdf.us2.list-manage.com/subscribe/post?u=87204b44efb46f0fd27b95167&amp;id=f511375e11'
EMAIL_SUBSCRIPTION_LABEL = u'Get Weekly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send Me Updates'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     '404'))
STATIC_PATHS = [
    'theme/images',
    'images',
    'archive',
    'pdfs',
    'extra/CNAME',
    'scripts',
]
ARTICLE_EXCLUDES = ['archive', 'pdfs', 'scripts']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
USE_SHORTCUT_ICONS = True
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TWITTER_USERNAME = 'mlissner'
GOOGLE_PLUS_PROFILE_URL = 'https://plus.google.com/+MikeLissner'

SOCIAL = (
    ('Twitter', 'http://twitter.com/mlissner'),
    ('Github', 'http://github.com/mlissner'),
    ('Email', 'mailto:mlissner+blog@michaeljaylissner.com'),
)
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

LANDING_PAGE_ABOUT = {
    #'title': 'I make things from atoms and bits',
    'details': """<p>My name is Mike Lissner. I am the founder and lead developer of
    <a href="http://freelawproject.com">Free Law Project</a> where I spend most
    of my time making <a href="https://www.courtlistener.com">CourtListener</a>,
    <a href="https://www.recapthelaw.org">RECAP</a>, and
    <a href="https://github.com/freelawproject/juriscraper/">Juriscraper</a>.</p>

    <p>I'm a big believer in technology's ability to make us happier, but like
    anybody who has been around a while, I know that nothing is ever as simple
    as it seems.</p>

    <p>I'm a grad from <a href="http://ischool.berkeley.edu">UC Berkeley's
    School of Information</a> and <a href="http://pitzer.edu">Pitzer
    College</a>. Between the two, I'm something of a liberal-minded techno-person
    with a dash of old school hippy.</p>
    """
}
PROJECTS = [
    {
        'name': 'CourtListener',
        'url': 'https://www.courtlistener.com',
        'description': 'A powerful search and awareness tool leveling the '
                       'legal field'
    },
    {
        'name': 'Juriscraper',
        'url': 'https://github.com/freelawproject/juriscraper/',
        'description': 'A tool to scrape judgements from hundreds of court '
                       'websites.'
    },
    {
        'name': 'Trim My Feeds',
        'url': 'https://bitbucket.org/mlissner/trim-my-feeds/overview',
        'description': 'A simple tool to strip dead RSS feeds from whatever reader you use.'
    },
    {
        'name': 'XPath Tester',
        'url': 'http://xpath.courtlistener.com',
        'description': 'Test XPath queries against text using <code>lxml</code>'
    },
    {
        'name': 'Swimlane Diagram Generator',
        'url': '/posts/2010/09/06/swimlane-diagram-generator-written-in-xslt/',
        'description': 'A pedagogical exercise to take XML, convert it to '
                       'Javascript and process that back into an SVG swimlane '
                       'diagram!'
    },
    {
        'name': 'Pacific Crest Trail Temperature Visualization',
        'url': '/pct-temperatures/',
        'description': 'A research and visualization project of 20,000 '
                       'temperature recordings along the PCT.'
    },
]
