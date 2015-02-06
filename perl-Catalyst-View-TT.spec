%define upstream_name    Catalyst-View-TT
%define upstream_version 0.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Catalyst TT View Class

License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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



