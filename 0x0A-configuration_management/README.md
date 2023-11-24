CONFIGURATION MANAGEMENT
AUTHOR Natalie Wanjiru Wanjiku
--------------------------------------------------------

- Configuration Management (CM), refers to the process of systematically handling changes to a system in a way that the system maintains it integrity overtime.

- Automation is the Heart of Configuration Management.

BENEFITS OF CM
----------------------

- Quick Provisioning of new servrers.
- Quick recovery from criticall threats.
- No more snowflake servers.
- Version control.

Popular CM Tools
------------------------

- Ansible
- Puppet
- Chef


- This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.


TASKS
------------------

0. Create a file


Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet


1. Install a package



Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0

2. Execute a command



Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill