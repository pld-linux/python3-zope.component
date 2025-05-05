#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (circular zope.security dependency)

%define module	zope.component
Summary:	Core of the Zope Component Architecture
Summary(pl.UTF-8):	Rdzeń Zope Component Architecture
Name:		python3-%{module}
Version:	6.0
Release:	1
License:	ZPL v2.1
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-%{version}.tar.gz
# Source0-md5:	55d4d24f425b18e2368a18c468f8cc47
Patch0:		zope.component-intersphinx.patch
URL:		https://www.zope.dev/
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-devel >= 1:3.7
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
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core of the Zope Component Architecture.

%description -l pl.UTF-8
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
%patch -P0 -p1

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
zope-testrunner-3 --test-path=src -v
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/zope/component
%{py3_sitescriptdir}/zope.component-%{version}-py*.egg-info
%{py3_sitescriptdir}/zope.component-%{version}-py*-nspkg.pth

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
