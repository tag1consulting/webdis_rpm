# The following software is released as specified below.
# This spec file is released to the public domain.

Name: webdis
Version: 0.1
Release: 1
Summary: A fast HTTP interface for Redis
Group:	Web
License: GPL
URL: http://webd.is
# Packager Information
Packager: Narayan Newton <nnewton@tag1consulting.com>
# Build Information
BuildRoot:	%{_tmppath}/%{name}-%{version}
# Source Information
Source0: webdis.0.1.478c62c66be1da120.tar.gz
Source1: webdis.initd
# Dependency Information
BuildRequires:	gcc binutils make libevent-devel
Requires: libevent 
%description
A fast HTTP interface for Redis, based on Libevent. Can return Redis objects in arrays, TXT, JSON and HTML.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=/usr
mkdir -pv %{buildroot}/etc/init.d
install -o root -g root -m 755 %{S:1} %{buildroot}/etc/init.d/webdis

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
/etc/webdis.prod.json
/usr/bin/webdis
/etc/init.d/webdis


%doc
%changelog
* Thu Dec 13 2011 Narayan Newton <nnewton@tag1consulting.com> 
- Initial Webdis Spec
* Sat Aug 29 2009 Robert Xu <robxu9@gmail.com> 
- Initial Spec File
