%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.jqplugins.flot

Name:           python-tw2-jqplugins-flot
Version:        2.0.1
Release:        3%{?dist}
Summary:        jQuery flot (plotting) for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# For building, generally
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tw2-core
BuildRequires:  python-tw2-excanvas
BuildRequires:  python-tw2-jqplugins-ui

# Specifically for the test suite
BuildRequires:  python-nose
BuildRequires:  python-formencode
BuildRequires:  python-BeautifulSoup
BuildRequires:  python-strainer
BuildRequires:  python-webtest

# Templating languages for the test suite
BuildRequires:  python-mako
BuildRequires:  python-genshi


# Runtime requirements
Requires:       python-tw2-core
Requires:       python-tw2-excanvas
Requires:       python-tw2-jqplugins-ui

%description
toscawidgets2 (tw2) aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

flot is a pure Javascript plotting library for jQuery. It produces graphical
plots of arbitrary data sets on-the-fly client-side.

This module, tw2.jqplugins.flot, provides toscawidgets2 (tw2) access
to flot widgets.

%prep
%setup -q -n %{modname}-%{version}

%if %{?rhel}%{!?rhel:0} >= 6

# Make sure that epel/rhel picks up the correct version of webob
awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"WebOb>=1.0\"]; import pkg_resources"}1' setup.py > setup.py.tmp
mv setup.py.tmp setup.py

# Remove all the fancy nosetests configuration for older python
rm setup.cfg

%endif


%build
%{__python} setup.py build
# This is a hack to get the jqplugins to not stomp all over each others
# namespace declarations.
rm -f build/lib/tw2/jqplugins/__init__.py*

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%check
PYTHONPATH=$(pwd) python setup.py test

%files
%doc README.rst LICENSE.txt

%{python_sitelib}/tw2/jqplugins/flot
%{python_sitelib}/%{modname}-%{version}-*

%changelog
* Mon May 07 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-3
- Updated directory ownership to avoid conflict with other tw2 packages

* Wed May 02 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Tue Apr 17 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- Package new version
- Fixes test suite

* Thu Apr 12 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora
