%define		_class		HTTP
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.4.1
Release:	%mkrel 5
Summary:	Miscellaneous HTTP utilities
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The HTTP class is a class with static methods for doing miscellaneous
HTTP-related stuff like date formatting or language negotiation.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-5mdv2011.0
+ Revision: 667512
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-4mdv2011.0
+ Revision: 607110
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-3mdv2010.1
+ Revision: 477892
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.1-2mdv2010.0
+ Revision: 426646
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 278923
- update to new version 1.4.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.0-3mdv2009.0
+ Revision: 224747
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2008.1
+ Revision: 178517
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2007.0
+ Revision: 81741
- Import php-pear-HTTP

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdk
- 1.4.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.6-1mdk
- 1.3.6

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.5-1mdk
- initial Mandriva package (PLD import)

