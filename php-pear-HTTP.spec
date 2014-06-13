%define _class		HTTP
%define modname	%{_class}

Summary:	Miscellaneous HTTP utilities
Name:		php-pear-%{modname}
Version:	1.4.1
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTTP/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml

