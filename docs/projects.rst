========
Projects
========

The vast majority of my projects are open source and can be found on
GitHub_. This is a list of projects I've written or contributed to in
some way. I love discussing them, so feel free to ask me about them.

##########
cargo-bump
##########

`cargo-bump`_ is a command that increases the version number of the rust project
you are currently in. It is meant to be a Rust version of npm version.

* A fun exercise in gluing libraries together in Rust.
* An interesting opportunity to work with others in the community who are
  writing Rust libraries.
* Started as a challenge to myself to build a Rust project from scratch in a
  night.

################
WeeChat Notifier
################

`weechat-notifier`_ is a daemon written in Rust meant to connect to a running
WeeChat_ session on another machine and provide notifications on the local
machine. I am writing it mostly as an experiment in writing a parser, client
library, and a daemon in Rust.

* Learned a valuable lesson about how writing a parser in a static language like
  you would in a dynamic language results in cumbersome code.
* Had a lot of fun experimenting with different testing styles.

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

* Core developer/maintainer on the project for a couple years.
* Wrote better integration with GitHub, including tests.
* Made it possible for multiple people be admins on a project.
* Took part in architecture discussions with the maintainer.
* Took over maintainership for 4 months while the previous maintainer was away.

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

#######
PDXNode
#######

This is less a software project and more a project that revolves around,
software. I was a co-organizer for the group for years, which meant planning
meetings, getting speakers, running workshops, and more.

* Once a month software hack night that I mentored at.
* Once a month hardware hack night which I was a core mentor for.
* Once a month presentation night, some months I filled in if we couldn't find a
  speaker.
* Periodic workshops, some I was the main organizer, others I was just a mentor.

########
Hardware
########

Since July or so of 2013, I've become a hardware hacker to complement my
software development skills. It is really great being able to interact with
the real world, not just via a keyboard or mouse or something.

* Built a monitoring system for my house, temp, light, humidity and cat door.
* Built a media keyboard (play/pause/back/forward/volume) where I had to patch
  the firmware that comes with the chip to better adhear to the USB HID spec.
* In the process of building a bike computer with GPS, heart rate, cadence and
  a light system.
* In the process of building a monitoring system for my smoker.

######
Resume
######

That would be this_. I have it up on GitHub because it is easier to
maintain there. It is written in ReStructured Text using sphinx so I
can host it on Read the Docs.

I was inspired by another user who has his resume_ on Read The Docs as
well!


.. _GitHub: https://github.com/wraithan
.. _`cargo-bump`: https://github.com/wraithan/cargo-bump
.. _`weechat-notifier`: https://github.com/weechat-notifier
.. _WeeChat: https://weechat.org
.. _`Read the Docs`: http://readthedocs.org/
.. _sphinx: http://sphinx.pocoo.org/
.. _ZenIRCBot: https://github.com/zenirc/zenircbot
.. _this: https://github.com/wraithan/resume
.. _resume: http://resume.readthedocs.org/
