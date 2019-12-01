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

BuildRequires: pyinstaller
Requires: rh-python3

%description
A Python tool for backing up files.

%prep
scl enable rh-python36 bash

%build
pyinstaller --onefile %{_sourcedir}/cli.py

%install
rm -rf %{buildroot}
mkdir -p /opt/python_backup_tool
cp %{_sourcedir}/dist/cli /opt/python_backup_tool/

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)