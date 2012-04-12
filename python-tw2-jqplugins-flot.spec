%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.jqplugins.flot

Name:           python-tw2-jqplugins-flot
Version:        2.0.0
Release:        1%{?dist}
Summary:        jQuery flot (plotting) for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# For building, generally
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tw2-core
BuildRequires:  python-tw2-excanvas
BuildRequires:  python-tw2-jqplugins-ui

# Specifically for the test suite
BuildRequires:  python-nose

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
plots of arbitrary datasets on-the-fly client-side.

This module, tw2.jqplugins.flot, provides toscawidgets2 (tw2) access
to flot widgets.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%check
PYTHONPATH=$(pwd) python setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE.txt
%{python_sitelib}/*

%changelog
* Thu Apr 12 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora