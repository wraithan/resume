======
Skills
======

This is a subset of my skills that I feel most comfortable with. I've
played with writing things ranging from graphics engines, to decoding
game save file formats, to window managers, to IRC bots, to web sites.

For a concise list of languages and time spent in them:

* 5+ years experience with Python, JavaScript, and SQL.
* 2+ years experience with C++, Perl, PHP, Java, and Lua.
* 1+ years experience with Haskell, C, and C#.
* Have played with many others including Common Lisp, Ruby, Go, and Clojure

######
Python
######

I've spent the last 5 years programming in Python, 3 of that was
professional. Most of my experience with Python is centered around
writing Django applications.

Some things I've built outside of web applications:

* A command line task management system
* Screen scrapers
* Feed aggregators
* Plugins and extensions for various tools that embed Python.

######
Django
######

If I am going to write a web app, and probably going to start with
``django-admin.py startproject <project name>``. I've been using it for
years now on projects both large and small. The community encourages
writing resuable code and sharing it which agrees strongly with how I
feel about writing software.

######
Celery
######

I use this when I need to offload tasks in Django based sites. Here
are a few things I have done with it:

* Helped architech and develop a lazy caching backend that updated
  itself out of band using Celery, or calculated in line if celery
  hadn't updated the cache yet.
* Divided tasks into separated queues so the Celery daemon could be
  shared to multiple servers.

######
Fabric
######

This tool has saved me hours, if not days of my life.

* I have ran 2 sprints on it, one PSF sponsored, the other at PyCon.
* Made deployment simple and very reproducible causing it to be fast
  and take care of all the repetitive details for the team.

#####
Redis
#####

I reach for this when I want a key/value store or centralized
pub/sub. I have use it for:

* Django caching backend.
* Django session storage.
* Celery queue backend (including connection pooling)
* Micro services based IRC bot using Redis' pub/sub as a transport.

##########
PostgreSQL
##########

This is my preferred relational database. It scales pretty well, it is
open source, and I've come to rely on it anytime I need a database.

* Have used tools such as pgfouine to profile and optimize usage.
* Used pgbouncer to do connection pooling to decrease latency.
* Have scaled to tables with millions of rows.

##########
JavaScript
##########

I've used it for many years now. Mostly doing front end work on the
web. But more recently I've also done things like building a Firefox
add-on, and many little micro-services.

######
jQuery
######

When I am doing JavaScript for the sake of front end development I
tend to lean on this library quite a bit for its selectors and other
niceties.

* Built many dynamic front ends using AJAX
* Built a Firefox Add-on that uses jQuery to build and modify most of
  the DOM.

##################
Firefox Add-on SDK
##################
I've only built one but plan on building more.

* An add-on for listing GitHub repos and quick links for them (code,
  issues, wiki, etc)


####
Node
####

Node is a recent addition to my bag of tricks. It sparked the fire in
me to really start enjoying JavaScript. I have been using it to build
out co-operative micro-services such as:

* An IRC bot.
* A layer for receiving web hooks.
* A GitHub post receive hook processor.
* Process management for all of these micro-services.
