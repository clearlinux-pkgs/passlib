#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4D8592DF4CE1ED31 (elic@astllc.org)
#
Name     : passlib
Version  : 1.7.1
Release  : 33
URL      : http://pypi.debian.net/passlib/passlib-1.7.1.tar.gz
Source0  : http://pypi.debian.net/passlib/passlib-1.7.1.tar.gz
Source99 : http://pypi.debian.net/passlib/passlib-1.7.1.tar.gz.asc
Summary  : comprehensive password hashing framework supporting over 30 schemes
Group    : Development/Tools
License  : BSD-3-Clause
Requires: passlib-python3
Requires: passlib-python
Requires: bcrypt
Requires: cryptography
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools

%description
cross-platform implementations of over 30 password hashing algorithms, as well
        as a framework for managing existing password hashes. It's designed to be useful
        for a wide range of tasks, from verifying a hash found in /etc/shadow, to
        providing full-strength password hashing for multi-user applications.

%package python
Summary: python components for the passlib package.
Group: Default
Requires: passlib-python3

%description python
python components for the passlib package.


%package python3
Summary: python3 components for the passlib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the passlib package.


%prep
%setup -q -n passlib-1.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523565714
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
