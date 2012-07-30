Name:		pyagent
Version:	1.0
Release:	1%{?dist}
Summary:	An agent for RHQ server providing data from CIM servers.
Group:		Applications/System
License:	GPLv3+
URL:		http://rhqagent.blogspot.com/
# The source for this package was pulled from upstream vcs.
# To get the source code, clone https://github.com/krzykwas/rhqagent.git
# and run `git archive HASH -o pyagent-HASH.tar` where HASH is included
# in the name of the archive with the source code (in Source0).
Source0:	pyagent-%{pyagent_git_commit}.tar
BuildRoot:	%{_topdir}/BUILDROOT/

BuildRequires:	python >= 2.7
Requires:	python >= 2.7, python < 3
Requires:	pywbem

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc

%changelog
