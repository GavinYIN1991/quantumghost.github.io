#!/usr/bin/env python

AUTHOR = 'QuantumGhost'
SITENAME = "QuantumGhost's Vault"
SITEURL = ''
THEME = "themes/attila"

PATH = 'content'
TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'zh-CN'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_METADATA = {
    'status': 'draft',
}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
PAGE_URL = 'pages/{slug}'

MENUITEMS = (
    ('博客', '/archives'),
    ('分类', '/categories'),
    ("标签", '/tags'),
    ("关于", '/pages/about'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['static', 'extra/CNAME', 'extra/robots.txt', 'extra/keybase.txt']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/keybase.txt': {'path': 'keybase.txt'}
}

# Blogroll

# Social widget
SOCIAL = (('Github', 'https://github.com/QuantumGhost'),
        ('Keybase', 'https://keybase.com/QuantumGhost'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
