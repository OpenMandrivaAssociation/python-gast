Summary:	Extract semantic information about static Python code
Name:		python-beniget
Version:	0.4.1
Release:	1
Group:		Development/Python
License:	BSD
URL:		https://github.com/serge-sans-paille/beniget/
#Source0:	https://github.com/serge-sans-paille/beniget/archive/%{version}/beniget-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/b/beniget/beniget-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
Beniget is a static analyzer for Python2 and Python3 code.

Beniget provides a static over-approximation of the global and local
definitions inside Python Module/Class/Function. It can also compute
def-use chains from each definition.

%files
%license LICENSE
%doc README.rst
%{py_sitedir}/beniget
%{py_sitedir}/beniget-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n beniget-%{version}

%build
%py_build
 
%install
%py_install

