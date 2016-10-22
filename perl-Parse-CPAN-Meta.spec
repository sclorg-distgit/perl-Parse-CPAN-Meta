%{?scl:%scl_package perl-Parse-CPAN-Meta}

Name:           %{?scl_prefix}perl-Parse-CPAN-Meta
# dual-lifed module needs to match the epoch in perl.spec
Epoch:          1
Version:        1.4422
Release:        2%{?dist}
Summary:        Parse META.yml and META.json CPAN meta-data files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parse-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Module Runtime
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.011
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(JSON::PP) >= 2.27300
BuildRequires:  %{?scl_prefix}perl(strict)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.80
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.82
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(YAML)
# Optional Tests
# CPAN::Meta needs Parse::CPAN::Meta
%if 0%{!?perl_bootstrap:1} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.120900
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Prereqs)
# To be able build dual-lifed module asap
# JSON is not core module and it needs CGI => Moo ...
BuildRequires:  %{?scl_prefix}perl(JSON) >= 2.5
%endif
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.011
Requires:       %{?scl_prefix}perl(Encode)
Requires:       %{?scl_prefix}perl(JSON::PP) >= 2.27300

%description
Parse::CPAN::Meta is a parser for META.json and META.yml files, using JSON::PP
and/or CPAN::Meta::YAML. It provides three methods: load_file,
load_json_string, and load_yaml_string. These will read and de-serialize CPAN
metafiles.

Parse::CPAN::Meta provides a legacy API of only two functions, based on the
YAML functions of the same name. Wherever possible, identical calling semantics
are used. These may only be used with YAML sources.

All error reporting is done with exceptions (die'ing).

%prep
%setup -q -n Parse-CPAN-Meta-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot} UNINST=0%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/Parse/
%{_mandir}/man3/Parse::CPAN::Meta.3*

%changelog
* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 1:1.4422-2
- SCL

* Sun Jul  3 2016 Paul Howarth <paul@city-fan.org> - 1:1.4422-1
- Update to 1.4422
  - Fixed use of Encode in load_json_string

* Wed Jun 29 2016 Paul Howarth <paul@city-fan.org> - 1:1.4421-1
- Update to 1.4421
  - Add CPAN_META_JSON_BACKEND to allow requesting non-JSON.pm backends
  - Add CPAN_META_JSON_DECODER to allow Mojo::JSON/JSON::Tiny to be used just
    for decoding
  - Re-encode strings before decode_json since that expects bytes
  - Add test cases for wide characters in META files
  - Bump JSON::PP prerequisite to 2.27300 to work around a bug before perl
    5.8.7; includes a test to confirm correct behavior
- BR: perl-generators
- Simplify find command using -delete

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4417-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4417-365
- Increase release to favour standalone package

* Tue Apr 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4417-4
- Don't BR: JSON when bootstrapping

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4417-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4417-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 Paul Howarth <paul@city-fan.org> - 1:1.4417-1
- Update to 1.4417
  - Outputs the version of backends used
  - Updated repo metadata and boilerplate files
  - Pointed issue tracker to the Perl-Toolchain-Gang Github repo
- Classify buildreqs by usage
- Use %%license
- Package CONTRIBUTING.mkdn and README files
- Expand %%description
- Make %%files list more explicit

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-312
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.4414-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4414-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  8 2014 Paul Howarth <paul@city-fan.org> - 1:1.4414-2
- Don't BR: CPAN::Meta & CPAN::Meta::Requirements when bootstrapping

* Wed Mar 12 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.4414-1
- Upstream update.
- Reflect upstream R:/BR:-changes.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:1.4404-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.4404-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Petr Pisar <ppisar@redhat.com> - 1:1.4404-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1:1.4404-2
- Perl 5.16 rebuild

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 1:1.4404-1
- update to latest upstream version

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 1:1.4403-1
- update to latest upstream version

* Wed Feb 08 2012 Iain Arnell <iarnell@gmail.com> 1:1.4402-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.4401-2
- Perl mass rebuild

* Wed Feb 16 2011 Iain Arnell <iarnell@gmail.com> 1:1.4401-1
- update to latest upstream version (removes Module::Load::Conditional dep)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 1:1.4400-1
- update to latest upstream version

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 1:1.4200-2
- install to vendorlib again

* Fri Jan 28 2011 Iain Arnell <iarnell@gmail.com> 1:1.4200-1
- Specfile autogenerated by cpanspec 1.78.
- bump epoch to match that in perl.spec
- install to privlib, not vendorlib

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-2
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-1
- new upstream version

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 1.39-2
- Bump for F12 mass rebuild

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.39-1
- auto-update to 1.39 (by cpan-spec-update 0.01)

* Mon Apr 27 2009 Ralf Corsépius <corsepiu@fedoraproject> - 0.05-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Steven Pritchard <steve@kspei.com> 0.04-1
- Update to 0.04.
- Update Source0 URL.
- Add version to Test::More dep.
- LICENSE and README went away.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.03-1
- Specfile autogenerated by cpanspec 1.75.
- BR Test::More.
