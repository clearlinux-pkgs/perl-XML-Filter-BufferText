#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Filter-BufferText
Version  : 1.01
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/R/RB/RBERJON/XML-Filter-BufferText-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RB/RBERJON/XML-Filter-BufferText-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-filter-buffertext-perl/libxml-filter-buffertext-perl_1.01-6.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-XML-Filter-BufferText-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::SAX)
BuildRequires : perl(XML::SAX::Base)

%description
XML::Filter::BufferText v0.01
=============================================================================

%package dev
Summary: dev components for the perl-XML-Filter-BufferText package.
Group: Development
Provides: perl-XML-Filter-BufferText-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-Filter-BufferText package.


%package license
Summary: license components for the perl-XML-Filter-BufferText package.
Group: Default

%description license
license components for the perl-XML-Filter-BufferText package.


%prep
%setup -q -n XML-Filter-BufferText-1.01
cd ..
%setup -q -T -D -n XML-Filter-BufferText-1.01 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-Filter-BufferText-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Filter-BufferText
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-Filter-BufferText/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/XML/Filter/BufferText.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Filter::BufferText.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Filter-BufferText/deblicense_copyright
