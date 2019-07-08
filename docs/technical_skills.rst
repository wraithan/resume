================
Technical Skills
================

This is a list of my stronger technical skills. I've played with
writing things ranging from graphics engines, to decoding game save
file formats, to window managers, to IRC bots, to web sites.

Language Skills:

* Deep understanding of Node.js.
* Have worked with Python, C++, and SQL in the recent past.
* Have played with Rust quite a bit.
* Have some work experience in the further past in PHP, Perl, and Java
* Others I've played with in some capacity or another: Lua, Haskell, Common
  Lisp, Clojure, and Go

#######
Node.js
#######

It sparked the fire in me to really start enjoying JavaScript. I have used it to
build out micro services, command line utilities, libraries, and for work.

* Have a deep understanding of performance in Node.js and V8.
* Wrote instrumentation for a number of database drivers and frameworks,
  requiring knowledge of the library internals.
* Wrote a benchmarking suite as a series of micro services that can run
  benchmarking and load testing jobs for days or weeks.
* Participated in various contributor discussions affecting the direction of
  Node.js for tracing and release cycle.
* Have played in lots of online AI games using JS.

####
Rust
####

This programming language is easily my favorite at the moment. The ownership
system and the type system both feel like a great advancement over other modern
languages. It has really reawakened my desire to work at the native layer instead
of in VMs.

* Primary language I use on the weekends for learning and small projects.
* Spent time reimplementing past Node.js AI bots of mine in Rust and seeing the
  differences in algorithms.
* Language of choice for code challenges like `Advent of Code <http://adventofcode.com/>`_
* Past few years of personal game development have been using this language.

######
Python
######

I've spent about 6 years programming in Python, 4 of that was
professional. Most of my experience with Python is centered around
writing Django applications.

Some things I've built outside of web applications:

* A command line task management system
* Screen scrapers
* Feed aggregators
* Plugins and extensions for various tools that embed Python.

------
Django
------

A couple years ago If I was going to write a web app, I would probably start
with ``django-admin.py startproject <project name>``. I used it for years on
projects both large and small.

Here are some highlights of from Django projects I've worked on.

* Three sites that shared the same code base and served a large number
  of users.
* OAuth2 (spec 10 and 11) based signup and authentication.
* Upgrading between multiple Django versions.
* Numerous community and small business sites.

------
Celery
------

I use this when I need to offload tasks in Django based sites. Here
are a few things I have done with it:

* Helped architech and develop a lazy caching backend that updated
  itself out of band using Celery, or calculated in line if celery
  hadn't updated the cache yet.
* Divided tasks into separated queues so the Celery daemon could be
  shared to multiple servers.

------
Fabric
------

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
* Chat system for a video game

##########
PostgreSQL
##########

This is my preferred relational database. It scales pretty well, it is
open source, and I've come to rely on it anytime I need a database.

* Have used tools such as pgfouine to profile and optimize usage.
* Used pgbouncer to do connection pooling to decrease latency.
* Have scaled to tables with millions of rows.

#####
MySQL
#####

Used this in a pretty large database (150+ tables) which required a deeper
understanding of relational algebra than I had previously. Learned many of the
quirks around time handling and strict mode SQL as I wrote queries to gather user
and game state from the database.

###
Git
###

I am commonly found teaching people how to use git, recover from
situations they and not sure how to get out of, and giving my opinions
on best practices based on experience and discussion with others that
have passion about how to use their version control system.

###
C++
###

Working on Dropzone at Sparkypants meant developing async C++ libraries for use by
the game client and game server to communicate to the backend services.

In working with hardware I've had to relearn and get better at C++. It was my
first language, so coming back to it after spending years doing other
development is quite a bit of fun. Most of the development has been for arduino
compatible chips, communicating with the outside world using serial.

I also have had to read a lot of C++ while inspecting the internals of Node.js
and V8, developing my ability to read other people's C++ in complex
environments.


########
BigQuery
########

Telemetry data at Cedexis/Citrix was shipped to this database, most of my work
with this database was finding was to effectively query many GB to TB of data
and get out statistically relevant insights out.