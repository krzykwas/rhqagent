Name:		pyagent
Version:	1.0
Release:	1%{?dist}
Summary:	An agent for RHQ server providing data from CIM servers.
Group:		Applications/System
License:	GPLv3+
URL:		http://rhqagent.blogspot.com/
# The source for this package was pulled from upstream vcs.
# To get the source code, clone https://github.com/krzykwas/rhqagent.git
# and run `git archive HASH -o pyagent-HASH.tar` where HASH is equal
# to the value of Source0.
Source0:	%{pyagent_git_commit}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	
Requires:	

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
