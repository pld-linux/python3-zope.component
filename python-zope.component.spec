#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		_enable_debug_packages	0

%define module	zope.component
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		python-%{module}
Version:	4.4.1
Release:	10
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-%{version}.tar.gz
# Source0-md5:	dc43aca08995751159e4b0f98f5afc5a
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core of the Zope Component Architecture.

%description -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%package -n python3-zope.component
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Group:		Libraries/Python

%description -n python3-zope.component
Core of the Zope Component Architecture.

%description -n python3-zope.component -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%prep
%setup -q -n zope.component-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install \
	--install-purelib=%{py_sitescriptdir}

%py_postclean
%endif

%if %{with python3}
%py3_install \
	--install-purelib=%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{with python2}
%{py_sitescriptdir}/zope/component
%{py_sitescriptdir}/zope.component-*.egg-info
%{py_sitescriptdir}/zope.component-*-nspkg.pth
%endif

%files -n python3-zope.component
%defattr(644,root,root,755)
%if %{with python3}
%{py3_sitescriptdir}/zope/component
%{py3_sitescriptdir}/zope.component-*.egg-info
%{py3_sitescriptdir}/zope.component-*-nspkg.pth
%endif
