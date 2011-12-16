========
Projects
========

The vast majority of my projects are open source and can be found on
GitHub_. In here I am going to highlight some of my favorite projects
to work on or ones with the coolest premise behind them.

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
sphinx, setting up a RTD project for them, and transfering ownership
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
crashes, it doens't take the bot down with it.

This was my first foray into using Node. IRC bots have become sort of
like a hello world to me when working in a new language. In this case
I orginally wrote the core IRC handling code myself to better
understand Node. Then I found node-irc_ and after fixing up their docs
so they were on RTD, cleaning up the code a bit, and adding some
needed features (and getting all of those pull requests accepted) I
switched my bot over to it.

This bot was developed mostly while I working at Aquameta_ and is a
core piece of infrastructure for them now. This is why the repo is
under their name.


.. _GitHub: https://github.com/wraithan
.. _geoloqi-workout-tracker: https://github.com/wraithan/geoloqi-workout-tracker
.. _Geoloqi: http://geoloqi.com/
.. _geoloqi-python: https://github.com/wraithan/geoloqi-python
.. _ZenIRCBot: https://github.com/aquameta/zenircbot
.. _node-irc: https://github.com/martynsmith/node-irc
.. _Aquameta: http://aquameta.com/
