#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : passlib
Version  : 1.6.5
Release  : 16
URL      : https://pypi.python.org/packages/source/p/passlib/passlib-1.6.5.tar.gz
Source0  : https://pypi.python.org/packages/source/p/passlib/passlib-1.6.5.tar.gz
Summary  : comprehensive password hashing framework supporting over 30 schemes
Group    : Development/Tools
License  : BSD-3-Clause
Requires: passlib-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========================
The Passlib Python Library
==========================

%package python
Summary: python components for the passlib package.
Group: Default

%description python
python components for the passlib package.


%prep
%setup -q -n passlib-1.6.5

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
