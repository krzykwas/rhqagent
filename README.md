rhqagent
========

What is this project about?

	Shortly: this project is an RHQ agent gathering metrics data from Fedora/RHEL hosts via 
Matahari and passing that data to an RHQ server.

What does it mean?

	Hosts running Fedora or Red Hat have various parameters that might be of interest for 
instance for system administrators, who would like them to be monitored. That parameters might 
include the processors' load, the disks' space occupancy or the main board temperature - just to 
give a brief description of the kind of data we may be interested in.
	Firstly, Matahari[1] is used to access this kind of data. Secondly, the gathered data is 
sent to an RHQ server[2], which is then used to maintain the data and act according to the 
requirements defined by the user.

Additional info

	The agent for RHQ server is implemented in Python. The project is a part of Google Summer of 
Code 2012 program. The mentor of this project is Heiko Rupp[3].

=====
[1] http://matahariproject.org/
[2] http://rhq-project.org/display/RHQ/Home
[3] https://community.jboss.org/people/pilhuhn
