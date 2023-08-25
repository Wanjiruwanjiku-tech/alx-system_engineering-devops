		Confguration Management
-----------------------------------------------

The term is broadly used to refer to Server Configuration Management. This is a way to systematically handle changes made to system whie maintaining its integrty overtime


Automation (The use of technology wherr huan input minimized) is the heart of Configuration Management for servers.

Automation Tools/CM tools
------------------------

There are a few CM tools ut for this project we will be using puppet

Install puppet
---------------
	$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
	$ apt-get install -y ruby-augeas
	$ apt-get install -y ruby-shadow
	$ apt-get install -y puppet


Install puppet-lint
-----------------------
	$ gem install puppet-lint
