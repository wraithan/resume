====
Gigs
====

My professional work in the software industry over the years. There is
a bit of time between jobs here and there where I was working
non-technical jobs and spending a lot of time on personal
:doc:`projects <\projects>` working to develop the skills needed to
work in the industry.

Sparkypants Studios
###################
Senior Backend Enginer (Feb '16 - Jun '17)
******************************************

I got an opportunity to work on a video game, which had always been a dream of
mine. As backend engineers we built the systems that stored data, matchmaking,
login, and provided C++ libraries for the client and game server engineers to use.
We used a microservice architecture written in Node.js, Python, SQL, and C++. Heavily
using RabbitMQ as our message bus and MySQL as our database.

* Redesigned the matchmaking backend to enable a confirm step before creating the game,
  while refactoring all data collection from the database to be just in time instead of
  up front eliminating a large class of bugs and AFK users.
* Built an automated deployment system for our staging environment, with fully automatic
  registration and decommissioning of game servers on top of systemd and ansible.
* Built and designed a full consent friend system to systemically prevent abuse where
  possible.
* Refactored a C++ wrapper around libcurl to standardize header parsing and error
  propagation, preventing accidentally ignored errors and making HTTP access code
  easier to write.

New Relic
#########
Node.js Agent Engineer (Apr '14 - Feb '16)
******************************************

My first full time gig working in Node.js, and it was an amazing experience. 
I've was able to connect with so much of the Node.js community via my work for
New Relic. The Node.js Agent is the library New Relic customers install in
their Node.js applications which monitors it and sends data back to New Relic
servers for analysis.

* Maintained a weekly release cadence for over 52 weeks in a row. Allowing the
  agent to respond quickly to the needs of our users.
* Ran a series of support training session giving our support engineers much
  deeper understanding of how Node and our agent works. Resulting is a large
  reduction in support escalations.
* Learned about the deep internals of Node.js and v8 in order to make our agent
  more accurate and performant.
* Wrote and designed systems that accounted for as many error cases as possible
  because an error in the agent could crash a user's system.

Contracting
###########
Web Developer (Oct '13 - Apr '14)
*********************************

I took on a few small contracts in this time, mostly though I spent my time
learning to be a better Node.js engineer as I wanted to take my career toward
more asynchronous programming.

Mozilla
#######
Web Developer (May '12 - Sept '13)
**********************************

This was my first time working in truly high scale development, both in
traffic and in team size. It was also my first gig working with a purely
remote team distributed across many time zones.

* Started out working on addons.mozilla.org, reworking the use of Redis as
  a part of the caching solution.
* Worked on security critical sections of the site including the blocklist
  that Firefox uses to shut down bad addons and extensions in the wild.
* Was moved over to working on marketplace.firefox.com as part of the payments
  team.
* Integrated with multiple payment providers and built the security pin portion
  of the site.
* Was involved in many of the architecture choices such as revamping
  deployment, moving to smaller services, and caching.

Aquameta
########
Senior Software Developer (Mar '10 - Feb '12)
*********************************************

I loved this company and learned a great deal while I was working there.
It is where I cut my teeth on Django apps that needed more than just some
more hardware thrown at them to scale.

* Was part of a team that implemented, maintained, and extended a
  large Django application that powered 3 sites.
* Scaled that application using celery for offloading and generous
  amounts of caching.
* Upgraded Django between major versions twice. From 1.1 to 1.2 and
  from 1.2 to 1.3.
* Wrote and encouraged the writing of both unit tests and functional
  tests.
* Wrote and maintained one click deployment scripts using Fabric.
* Interfaced with the clients regularly to gather requirements for
  features.
* Guided the architecture of the application using community best
  practices and past experience.

Parthenon Software
##################
Software Developer (Sept '09 - Nov '09)
***************************************

This was a PHP shop I worked at for a short while. I did development
on a well established code base.

* Updated unit tests, allowing for more confidence that application
  was correct.
* Met with clients to discuss and advise on what course to take for
  re-designing their software.
* Implemented feature requests, fixing existing bugs in the module
  while adding the feature, resulting in cleaner, better documented
  code.
* Participated in “brainstorming” sessions concerning design/testing
  details for various project.

Critical Path Software
######################
QA Tester (May '08 - Aug '08)
*****************************

Here I worked in the QA department testing software and hardware. The
primary project I was hired for were 2 lines of computers that a
company was going to release and they wanted some independent stress
testing done in a wide range of activities. Online gaming, word
processing, downloading content, watching HD video both streaming and
off a Blu-Ray.

* Learned to write very effective bug reports.
* Wrote and executed test plans, tracking progress and reporting
  defects.
* Worked with a team to decide on software milestones and
  requirements.
* Set up many different hardware/software configurations for testing.
* Wrote a tool using C++ to generate data for testing.
* Assist in delegation of various portions of testing to help train
  new members of the team prior to product release.


Transim Technology
##################
Intern Software Developer (Dec '05 - Aug '06)
*********************************************

This was my first foray into the world of software development at a
company. The stack was a large java backend with a PHP layer on top
with liberal use of Perl as glue.

* Cleaned up and maintained several in-house tools written in Perl,
  Java, and PHP for processing and displaying circuit schematics.
* Created a GUI for two of the in-house tools so that non-technical
  staff could assist in processing schematics that needed human
  interaction.
* Implemented a secure login system with detailed permission setup.
* Documented all of the above mentioned work, along with a large
  portion of a Java based webserver back-end.

I had a great time at this job and this, on top of my passion I
already had, really sealed the deal as far as my desire to pursue
software development as my career.
