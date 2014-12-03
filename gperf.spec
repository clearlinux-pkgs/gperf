#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gperf
Version  : 3.0.4
Release  : 8
URL      : http://ftp.gnu.org/pub/gnu/gperf/gperf-3.0.4.tar.gz
Source0  : http://ftp.gnu.org/pub/gnu/gperf/gperf-3.0.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: gperf-bin
Requires: gperf-data
Requires: gperf-doc

%description
This is GNU gperf. It is a program that generates perfect hash
functions for sets of key words.  A perfect hash function is:

%package bin
Summary: bin components for the gperf package.
Group: Binaries
Requires: gperf-data

%description bin
bin components for the gperf package.


%package data
Summary: data components for the gperf package.
Group: Data

%description data
data components for the gperf package.


%package doc
Summary: doc components for the gperf package.
Group: Documentation

%description doc
doc components for the gperf package.


%prep
%setup -q -n gperf-3.0.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make check ||:

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gperf

%files data
%defattr(-,root,root,-)
/usr/share/doc/gperf.html

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
