%define module gast

Name:		python-gast
Version:	0.7.0
Release:	1
Summary:	Python AST that abstracts the underlying Python version
Group:		Development/Python
License:	BSD
URL:		https://github.com/serge-sans-paille/gast/
Source0:	https://github.com/serge-sans-paille/gast/archive/%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A generic AST to represent Python2 and Python3’s Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-*.*-info
