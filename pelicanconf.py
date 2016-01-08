# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Mehmet Köse'
SITENAME = "Mehmet' log"
SITEURL = 'http://localhost:8000'
TIMEZONE = "Europe/Paris"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

FEED_ALL_RSS = 'all.rss.xml'

LINKS = (('Biologeek', 'http://biologeek.org'),
         ('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),)

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}
