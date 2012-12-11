%define upstream_name    Catalyst-View-TT
%define upstream_version 0.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst TT View Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz
# This patch done originally by rgs allow to specify the Template class to use
# Need for compatibility with CS4 for fibric
Patch0:		Catalyst-View-TT-0.30-template_class.patch

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.700
BuildRequires:  perl(MRO::Compat)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Template)
BuildRequires:  perl(Template::Provider::Encoding)
BuildRequires:	perl(Template::Timer)

BuildArch:	noarch

%description
This is the Catalyst view class for the Template Toolkit. Your application
should defined a view class which is a subclass of this module. The easiest way
to achieve this is using the myapp_create.pl script (where myapp should be
replaced with whatever your application is called). This script is created as
part of the Catalyst setup.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p2

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.360.0-2mdv2011.0
+ Revision: 680771
- mass rebuild

* Mon Oct 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 589296
- New version - 0.36

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-1mdv2011.0
+ Revision: 573789
- update to 0.35

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 532707
- update to 0.34

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.1
+ Revision: 518076
- update to 0.33

* Tue Feb 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2010.1
+ Revision: 506742
- update to 0.32

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.1
+ Revision: 461263
- update to 0.31

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 450060
- fix require - using perl-Foo instead of perl(Foo) is bad, mmk?
- patch renamed, fix spec file
- update to 0.30

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.0
+ Revision: 406313
- rebuild using %%perl_convert_version

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2009.1
+ Revision: 343867
- update to new version 0.29

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 343199
- update to new version 0.28

* Tue Jun 17 2008 Olivier Thauvin <nanardon@mandriva.org> 0.27-2mdv2009.0
+ Revision: 222183
- resurect template_class patch done by rgs
- yet another buildrequires for tests

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2009.0
+ Revision: 210859
- new version

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2008.1
+ Revision: 153976
- update to new version 0.26

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2008.0
+ Revision: 47033
- update to new version 0.25


* Mon May 29 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.23-2mdv2007.0
- Patch 0: allow to override the internal template class

* Sat May 27 2006 Scott Karns <scottk@mandriva.org> 0.23-1mdv2007.0
- 0.23

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.22-3mdk
- Update BuildRequires
- Updated to comply with Mandriva perl packaging policy

* Mon Mar 06 2006 Buchan Milne <bgmilne@mandriva.org> 0.22-2mdk
- BuildRequire newer Catalyst (ease backport)

* Fri Jan 27 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.22-1mdk
- 0.22

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.21-1mdk
- 0.21

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-1mdk
- Initial MDV RPM

