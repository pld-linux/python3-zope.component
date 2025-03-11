#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (circular zope.security dependency)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define module	zope.component
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		python-%{module}
# keep 5.x here for python2 support
Version:	5.1.0
Release:	3
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-%{version}.tar.gz
# Source0-md5:	40f0fa6d002d443dad7dab2e11f2d79f
URL:		https://www.zope.dev/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-persistent
BuildRequires:	python-zope.configuration
BuildRequires:	python-zope.deferredimport >= 4.2.1
BuildRequires:	python-zope.deprecation >= 4.3.0
BuildRequires:	python-zope.event
BuildRequires:	python-zope.hookable >= 4.2.0
BuildRequires:	python-zope.i18nmessageid
BuildRequires:	python-zope.interface >= 5.3.0
BuildRequires:	python-zope.location
BuildRequires:	python-zope.proxy
BuildRequires:	python-zope.security
BuildRequires:	python-zope.testing
BuildRequires:	python-zope.testrunner
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-persistent
BuildRequires:	python3-zope.configuration
BuildRequires:	python3-zope.deferredimport >= 4.2.1
BuildRequires:	python3-zope.deprecation >= 4.3.0
BuildRequires:	python3-zope.event
BuildRequires:	python3-zope.hookable >= 4.2.0
BuildRequires:	python3-zope.i18nmessageid
BuildRequires:	python3-zope.interface >= 5.3.0
BuildRequires:	python3-zope.location
BuildRequires:	python3-zope.proxy
BuildRequires:	python3-zope.security
BuildRequires:	python3-zope.testing
BuildRequires:	python3-zope.testrunner
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-repoze.sphinx.autointerface
BuildRequires:	python3-zope.deferredimport >= 4.2.1
BuildRequires:	python3-zope.deprecation >= 4.3.0
BuildRequires:	python3-zope.event
BuildRequires:	python3-zope.hookable >= 4.2.0
BuildRequires:	python3-zope.interface >= 5.3.0
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
Provides:	Zope-Component
Obsoletes:	Zope-Component < 4
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
Requires:	python3-modules >= 1:3.5

%description -n python3-zope.component
Core of the Zope Component Architecture.

%description -n python3-zope.component -l pl.UTF-8
Rdzeń architektury komponentowej Zope Component Architecture.

%package apidocs
Summary:	API documentation for Python zope.deferredimport module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona zope.deferredimport
Group:		Documentation

%description apidocs
API documentation for Python zope.deferredimport module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona zope.deferredimport.

%prep
%setup -q -n zope.component-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py_sitescriptdir}/zope/component
%{py_sitescriptdir}/zope.component-%{version}-py*.egg-info
%{py_sitescriptdir}/zope.component-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-zope.component
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/component
%{py3_sitescriptdir}/zope.component-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.component-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
