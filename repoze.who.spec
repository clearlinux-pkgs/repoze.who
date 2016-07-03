#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : repoze.who
Version  : 2.3
Release  : 17
URL      : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Source0  : http://pypi.debian.net/repoze.who/repoze.who-2.3.tar.gz
Summary  : repoze.who is an identification and authentication framework for WSGI.
Group    : Development/Tools
License  : ZPL-2.1
Requires: repoze.who-python
BuildRequires : WebOb-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface-python

%description
``repoze.who``
==============
.. image:: https://travis-ci.org/repoze/repoze.who.png?branch=master
:target: https://travis-ci.org/repoze/repoze.who

%package python
Summary: python components for the repoze.who package.
Group: Default
Requires: WebOb-python
Requires: zope.interface-python

%description python
python components for the repoze.who package.


%prep
%setup -q -n repoze.who-2.3

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
