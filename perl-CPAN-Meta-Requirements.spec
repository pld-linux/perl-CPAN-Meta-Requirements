#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	CPAN
%define		pnam	Meta-Requirements
Summary:	CPAN::Meta::Requirements - a set of version requirements for a CPAN dist
Summary(pl.UTF-8):	CPAN::Meta::Requirements - zbiór wymaganych wersji dla dystrybucji CPAN
Name:		perl-CPAN-Meta-Requirements
Version:	2.143
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b26ca50ca6eb04f727876da83b828241
URL:		https://metacpan.org/dist/CPAN-Meta-Requirements
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-version >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A CPAN::Meta::Requirements object models a set of version constraints
like those specified in the META.yml or META.json files in CPAN
distributions. It can be built up by adding more and more constraints,
and it will reduce them to the simplest representation.

Logically impossible constraints will be identified immediately by
thrown exceptions.

%description -l pl.UTF-8
Obiekt CPAN::Meta::Requirements modeluje zbiór ograniczeń wersji,
takich jak te podawane w plikach META.yml lub META.json w
dystrybucjach CPAN. Mogą być tworzone poprzez dodawanie kolejnych
ograniczeń, a obiekt zredukuje je do najprostszej reprezentacji.

Ograniczenia logicznie niemożliwe zostaną zidentyfikowane natychmiast
poprzez rzucenie wyjątku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CPAN/Meta/Requirements.pm
%{perl_vendorlib}/CPAN/Meta/Requirements
%{_mandir}/man3/CPAN::Meta::Requirements.3pm*
%{_mandir}/man3/CPAN::Meta::Requirements::Range.3pm*
