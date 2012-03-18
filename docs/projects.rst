========
Projects
========

The vast majority of my projects are open source and can be found on
GitHub_. This is a list of projects I've written or contributed to in
some way. I love discussing them, so feel free to ask me about them.

#############
Read the Docs
#############

`Read the Docs`_ is a site for building and hosting sphinx_
documentation. The main goal of it is to lower the barrier to writing
docs as much as possible. The idea is that if there is free hosting,
automated building, and easy to select themes developers would write
docs. Once they are written maintaining them is easy because when you
push your docs are automatically rebuilt.

This is not a project that I built, but is a project that I contribute
to as well as help as support on. I can be commonly found taking some
poorly maintained docs for a project I am using and converting them to
sphinx, setting up a RTD project for them, and transferring ownership
to the author. That way instead of docs being a random markdown file
in a repo, it has a nice url and theme.

#######################
geoloqi-workout-tracker
#######################

geoloqi-workout-tracker_ is currently just a web interface that uses
OAuth2 to log into Geoloqi_, then lets you start and stop workouts. It
will soon let you associate your account with your DailyMile account
(and others as I figure out their terms of usage on their APIs or they
start to provide an API). Upon stopping a workout it will gather your
route data from Geoloqi then ship it to which ever workout trackers
you have associated for that type of workout.

It came from wanting to write something using the Geoloqi_ platform. I
started writing this because I found it quite dumb to have to run a
workout tracker, as well as a location tracker for quantified self
stuff. Also Geoloqi provides a way to share my location so when doing
long bike rides (such as to the coast) and my friends and family are
concerned they can watch my progress.

--------------
geoloqi-python
--------------

geoloqi-python_ is a support library for geoloqi-workout tracker that
others expressed interest in using at a Geoloqi hackathon. So I broke
it out and made it available. It is a very thin wrapper around
Geoloqi's API and will be more fleshed out as I use it more.

#########
ZenIRCBot
#########

ZenIRCBot_ is a IRC bot that works a bit differently than your
standard bot. I thought it was silly to have to restart my bot
whenever I wanted to add or remove a feature. Instead I chose to using
Redis' pub/sub functionality and have what would be plugins run as
services along side of the bot. An added benefit is if a service
crashes, it doesn't take the bot down with it.

This was my first foray into using Node. IRC bots have become sort of
like a hello world to me when working in a new language. In this case
I originally wrote the core IRC handling code myself to better
understand Node. Then I found node-irc_ and after fixing up their docs
so they were on RTD, cleaning up the code a bit, and adding some
needed features (and getting all of those pull requests accepted) I
switched my bot over to it.

#############
webhook-relay
#############

webhook-relay_ is a service I was architecting  to fill a hole in
gluing webhooks together as well as making webhooks more robust. The
original feature I wanted was a way to mutliplex and redirect an
incoming webhook. For example, I have almost all of the repos I
commonly work on, on RTD, also I have my IRC bot listening for GitHub
post receive hooks. It seems silly to setup both of them on every
repo, and if one of the URLs changes I have to go through all of my
projects and change them.

This provides a solution by having hooks, which are urls listening for
callbacks from webhooks. Then you associate it with at least one
emitter. In the above use case I'd have a software project hook, and a
couple callback emitters, one pointed at my bot, one pointed at Read
the Docs. Then if I ever moved where my bot was hosted, I could easily
change the url in the emitter and have all of my repos update
automatically. Also I only have to add one URL to my post receive
hooks on GitHub.

######
Resume
######

That would be this_. I have it up on GitHub because it is easier to
maintain there. It is written in ReStructured Text using sphinx so I
can host it on Read the Docs. This way I get a clean looking resume
that I can export as a PDF, or just directly link to.

I was inspired by another user who has his resume_ on Read The Docs as
well!


.. _GitHub: https://github.com/wraithan
.. _`Read the Docs`: http://readthedocs.org/
.. _sphinx: http://sphinx.pocoo.org/
.. _geoloqi-workout-tracker: https://github.com/wraithan/geoloqi-workout-tracker
.. _Geoloqi: http://geoloqi.com/
.. _geoloqi-python: https://github.com/wraithan/geoloqi-python
.. _ZenIRCBot: https://github.com/wraithan/zenircbot
.. _node-irc: https://github.com/martynsmith/node-irc
.. _webhook-relay: https://github.com/wraithan/webhook-relay
.. _this: https://github.com/wraithan/resume
.. _resume: http://resume.readthedocs.org/
