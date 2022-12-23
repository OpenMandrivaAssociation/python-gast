Summary:	Python AST that abstracts the underlying Python version
Name:		python-gast
Version:	0.5.3
Release:	1
Group:		Development/Python
License:	BSD
URL:		https://github.com/serge-sans-paille/gast/
#Source0:	https://github.com/serge-sans-paille/gast//archive/%{version}/gast-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/g/gast/gast-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
A generic AST to represent Python2 and Python3’s Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.

%files
%license LICENSE
%doc README.rst
%{py_sitedir}/gast
%{py_sitedir}/gast-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n gast-%{version}

%build
%py_build
 
%install
%py_install

