Name:		pyagent
Version:	%{version}
Release:	1%{?dist}
Summary:	An agent for RHQ server providing data from CIM servers.
Group:		Applications/System
License:	GPLv3+
URL:		http://rhqagent.blogspot.com/
# The source for this package was pulled from upstream vcs.
# To get the source code, clone https://github.com/krzykwas/rhqagent.git
# and run `git archive HASH -o pyagent-VERSION-HASH.tar` where both
# VERSION and HASH are included in the name of an archive
# with the source code (Source0).
Source0:	pyagent-%{version}-%{pyagent_git_commit}.tar
BuildRoot:	%{_topdir}/BUILDROOT/

BuildRequires:	python >= 2.7
Requires:	python >= 2.7, python < 3
Requires:	pywbem

BuildArch:	noarch

%description
RHQ agent gathering data from CIM servers
-----------------------------------------

	With a single agent instance you can simultaneously gather data
from many CIM instances and send them to many RHQ servers. You can even
compute so called artificial metrics on your own by defining and using
callbacks. This way you can combine several CIM metrics and create
a brand new one on your own.

	If you wish, you can quite easily extend the agent so that it
was able to communicate with different protocols as well - for that you
have to implement a suitable data provider and/or sender. As a simple
example, you might want to send data to a flat file or a database
or get it from such a source.

	The agent includes an interactive configuration file generator.

	This version depends on a python-wbem library to be able to
communicate with CIM servers using a CIM-XML protocol. This library is
Python 2.x-only and unless you'll implement a provider for another data
source, you are bound to Python 2.x. Nevertheless there should be few
changes needed to make the agent work with Python 3 if any at all.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -pv %{buildroot}/etc/%{name}
touch %{buildroot}/etc/%{name}/settings.xml

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%doc COPYING
%config(missingok) %ghost /etc/%{name}/settings.xml
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}-*.egg-info
/usr/bin/pyagent.py
/etc/init.d/run-pyagent.sh

%changelog
