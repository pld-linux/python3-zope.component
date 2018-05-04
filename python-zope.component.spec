%define module	zope.component
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		python-%{module}
Version:	4.4.1
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-%{version}.tar.gz
# Source0-md5:	dc43aca08995751159e4b0f98f5afc5a
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-zope.deferredimport
Requires:	python-zope.deprecation
Requires:	python-zope.event
Requires:	python-zope.interface
Requires:	python-zope.proxy
Requires:	python-zope.testing
Requires:	python-modules
Obsoletes:	Zope-Component
Provides:	Zope-Component
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core of the Zope Component Architecture.

%description -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%prep
%setup -q -n zope.component-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--install-purelib=%{py_sitedir} \

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/component
%{py_sitedir}/zope.component-*.egg-info
%{py_sitedir}/zope.component-*-nspkg.pth
