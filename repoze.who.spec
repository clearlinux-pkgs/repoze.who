#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : repoze.who
Version  : 2.3
Release  : 33
URL      : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Source0  : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Source1  : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz.asc
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
cd %{_builddir}/repoze.who-2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576015080
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/repoze.who
cp %{_builddir}/repoze.who-2.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/repoze.who/1c2024cb6cdcf19ca3e2c81c82936bc7596799c7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/repoze.who/1c2024cb6cdcf19ca3e2c81c82936bc7596799c7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
