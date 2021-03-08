#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = '星索'
SITENAME = '星索 Blog'
SITEURL = 'https://blog.xsnet.top'
ROBOTS = "index"
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese (Simplified)'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PLUGIN
PLUGIN_PATH = "pelican-plugins"
PLUGINS = ["render_math"]
# Theme
MAIN_MENU = True
THEME = "pelican-themes/Flex"
SITETITLE = "星索 Blog"
SITESUBTITLE = "发现生活，记录成长"
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
# Blogroll
LINKS = (
        )

# Social widget
SOCIAL = (
          ("rss", "https://blog.xsnet.top/feeds/all.atom.xml"),
          
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True