#
# Meteor RPM spec file
#

Summary: Meteor microframework and JavaScript application server
Vendor: Meteor
Name: meteor
Version: 0.1.4
Release: 1
License: AGPL-3
Group: Networking/WWW
Packager: Meteor Packaging Team <contact@meteor.com>
URL: http://meteor.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
XXX

%prep

%build

%install
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}
# XXX XXX
tar -x -C %{buildroot}%{_libdir} -f %{TARBALL}
install -d %{buildroot}%{_bindir}
ln -s /%{_libdir}/meteor/bin/meteor %{buildroot}%{_bindir}/meteor

%clean
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/meteor
%{_libdir}/meteor