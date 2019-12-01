%define name python-backup-tool
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1

Summary: Python Backup Tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Turbo Python <office@realpython.com>
Url: https://github.com/pythonredhat/python-backup-tool

#BuildRequires: pyinstaller
Requires: rh-python3

%description
A Python tool for backing up files.

#%prep
#scl enable rh-python36 bash

%build
/opt/rh/rh-python36/root/usr/bin/pyinstaller --onefile /root/rpmbuild/SOURCES/cli.py

%install
mkdir -p /opt/python_backup_tool2
cp /root/rpmbuild/SOURCES/dist/cli /opt/python_backup_tool/

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)