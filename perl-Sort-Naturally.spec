%define upstream_name    Sort-Naturally
Name:		perl-%{upstream_name}
Version:	1.03
Release:	5

Summary:	Sort lexically, but sort numeral parts numerically
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bingos/sort-naturally
Source0:	https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-1.03.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module exports two functions, 'nsort' and 'ncmp'; they are used in
implementing my idea of a "natural sorting" algorithm. Under natural
sorting, numeric substrings are compared numerically, and other
word-characters are compared lexically.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/Sort


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 404392
- rebuild using %1.03 Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-2mdv2009.0
+ Revision: 268724
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 213615
- import perl-Sort-Naturally


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
- first mdv release 

