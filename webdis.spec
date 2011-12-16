# The following software is released as specified below.
# This spec file is released to the public domain.

Name: webdis
Version: 0.1
Release: 2
Summary: A fast HTTP interface for Redis
Group:	Web
License: GPL
URL: http://webd.is
BuildRoot:	%{_tmppath}/%{name}-%{version}
# Source is on github git://github.com/nicolasff/webdis.git
Source0: webdis.0.1.478c62c66be1da120.tar.gz
Source1: webdis.initd
BuildRequires:	binutils libevent-devel
Requires: libevent chkconfig initscripts
%description
A fast HTTP interface for Redis, based on Libevent. Can return Redis objects in arrays, TXT, JSON and HTML.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_usr}
%{__install} -Dp -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add %{name} || :

%preun 
if [ "$1" = 0 ] ; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name} || :
fi

%postun
if [ "$1" -ge 1 ]; then
  /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%{_sysconfdir}/webdis.prod.json
%{_bindir}/webdis
%{_initrddir}/webdis


%changelog
* Thu Dec 13 2011 Jeff Sheltren <jeff@tag1consulting.com>
- Spec cleanup per Fedora guidelines
- Add chkconfig calls to post scripts

* Thu Dec 13 2011 Narayan Newton <nnewton@tag1consulting.com> 
- Initial Webdis Spec

* Sat Aug 29 2009 Robert Xu <robxu9@gmail.com> 
- Initial Spec File
