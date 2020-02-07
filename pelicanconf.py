#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fábio Mendes'
SITENAME = 'Curió Geek'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Porto_Velho'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Ars Technica', 'https://arstechnica.com/'),
         ('Wikipedia', 'https://wikipedia.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/fabiomendesilva'),
         ('Github', 'https://github.com/FabioMen10'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../output'

THEME = 'theme'

PLUGIN_PATHS = ['plugins/', ]

PLUGINS = ['i18n_subsites', 'jinja2content']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

JINJA2CONTENT_TEMPLATES = 'content'

BOOTSTRAP_THEME = 'flatly'

PYGMENTS_STYLE = 'monokai'
