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
* Patched various third party libraries to enable features in each of
  the bots.

##################
GitHub Repo Widget
##################

`GitHub Repo Widget`_ is a Firefox add-on that I wrote because I was
on bad internet and wanted faster access to my issue tracker.

* Used the Jetpack Add-on SDK which is written in JavaScript.
* Wrote my own lib for interacting with GitHub
* Found and submitted several bug reports against addons.mozilla.org
  and the add-on SDk.

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

webhook-relay_ is a service I was architecting to fill a hole in
gluing webhooks together as well as making webhooks more robust.

* Forward and multiplex incoming webhooks using celery.

################
aichallenge-ants
################

This was `my entry`_ into aichallenge_ for the ants competition.

* Wrote a custom weight dispersion algorithm.
* Used PyPy.

#####
speck
#####

speck_ command line interface to `letsfreckle`_.

* Used baker_ to do the command line argument and function parsing
  easier.
* Interacted with an external REST API.

######
Fabric
######

Fabric_ is a library to make remote system management easier. While
I've not directly contributed to Fabric, I have run multiple code
sprints for it.

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
.. _`GitHub Repo Widget`: https://addons.mozilla.org/en-US/firefox/addon/github-repo-widget/
.. _geoloqi-workout-tracker: https://github.com/wraithan/geoloqi-workout-tracker
.. _Geoloqi: http://geoloqi.com/
.. _geoloqi-python: https://github.com/wraithan/geoloqi-python
.. _ZenIRCBot: https://github.com/wraithan/zenircbot
.. _node-irc: https://github.com/martynsmith/node-irc
.. _webhook-relay: https://github.com/wraithan/webhook-relay
.. _this: https://github.com/wraithan/resume
.. _resume: http://resume.readthedocs.org/
.. _aichallenge: http://aichallenge.org/
.. _letsfreckle: http://letfreckle.com/
.. _baker: http://pypi.python.org/pypi/Baker/
.. _speck: https://github.com/wraithan/speck
.. _`my entry`: https://github.com/wraithan/aichallenge-ants
.. _Fabric: http://fabfile.org/
