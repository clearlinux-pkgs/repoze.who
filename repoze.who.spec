#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : repoze.who
Version  : 2.3
Release  : 32
URL      : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Source0  : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Source99 : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz.asc
Summary  : repoze.who is an identification and authentication framework for WSGI.
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.who-license = %{version}-%{release}
Requires: repoze.who-python = %{version}-%{release}
Requires: repoze.who-python3 = %{version}-%{release}
Requires: WebOb
Requires: setuptools
Requires: zope.interface
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
==============

%package license
Summary: license components for the repoze.who package.
Group: Default

%description license
license components for the repoze.who package.


%package python
Summary: python components for the repoze.who package.
Group: Default
Requires: repoze.who-python3 = %{version}-%{release}

%description python
python components for the repoze.who package.


%package python3
Summary: python3 components for the repoze.who package.
Group: Default
Requires: python3-core

%description python3
python3 components for the repoze.who package.


%prep
%setup -q -n repoze.who-2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541278389
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/repoze.who
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/repoze.who/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/repoze.who/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
