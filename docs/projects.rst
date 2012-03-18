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

What I did for the project:

* Wrote better integration with GitHub, including tests.
* Made it possible for multiple people be admins on a project.
* Took part in architecture discussions with the maintainer.

#########
ZenIRCBot
#########

ZenIRCBot_ is a IRC bot that works a bit differently than your
standard bot. Features (and interesting to implement things) include:

* Microservice architecture
* Redis pub/sub as a transport
* Services can be written in any language.
* Core bot written in Node.js but reference implementations are also
  in Python and Clojure.

#######################
geoloqi-workout-tracker
#######################

geoloqi-workout-tracker_ is my stab at building something on the
Geoloqi_ platform. Interesting bits of this:

* Register new accounts and login using Geoloqi's OAuth2 service.
* Associate accounts with DailyMile using OAuth2.

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
