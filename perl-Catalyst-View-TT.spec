%define upstream_name    Catalyst-View-TT
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Catalyst TT View Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz
# This patch done originally by rgs allow to specify the Template class to use
# Need for compatibility with CS4 for fibric
Patch0:     Catalyst-View-TT-0.30-template_class.patch

BuildRequires:	perl-Catalyst >= 5.50
BuildRequires:  perl(MRO::Compat)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Template)
BuildRequires:  perl(Template::Provider::Encoding)
BuildRequires:	perl(Template::Timer)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
