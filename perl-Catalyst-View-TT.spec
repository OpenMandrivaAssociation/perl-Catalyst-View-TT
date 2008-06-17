%define module Catalyst-View-TT
%define name	perl-%{module}
%define	modprefix Catalyst
%define version	0.27
%define release	%mkrel 2

Summary:	Catalyst TT View Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
# This patch done originally by rgs allow to specify the Template class to use
# Need for compatibility with CS4 for fibric
Patch0:     Catalyst-View-TT-template_class.patch
BuildRequires:	perl-Catalyst >= 5.50
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Template)
BuildRequires:	perl(Template::Timer)
BuildRequires:  perl(Template::Provider::Encoding)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This is the Catalyst view class for the Template Toolkit. Your application
should defined a view class which is a subclass of this module. The easiest way
to achieve this is using the myapp_create.pl script (where myapp should be
replaced with whatever your application is called). This script is created as
part of the Catalyst setup.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}

