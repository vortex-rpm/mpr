Name:           mpr
Version:        1.1
Release:        1.vortex%{?dist}
Summary:        \m/ Package Repository

Group:          Applications/System
License:        MIT
URL:            https://github.com/greevex/mpr
Source0:        https://github.com/downloads/greevex/%{name}/%{name}_client-1.1.src.tar.gz
Patch0:		path_to_libs.patch
Vendor:		Vortex RPM
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       php54

%description
\m/ Package Repository
Also may be "\m/ Phar Repository" ;)


%prep
%setup -n client
%patch0 -p0
perl -pi -e "s|/usr/lib|%{_libdir}|g" %{name}.run.php


%install
rm -rf $RPM_BUILD_ROOT
install -D -m 644 %{name}.php $RPM_BUILD_ROOT/%{_libdir}/%{name}/%{name}.php
install -D -m 644 helper.php $RPM_BUILD_ROOT/%{_libdir}/%{name}/helper.php
install -D -m 755 %{name}.run.php $RPM_BUILD_ROOT/%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/%{name}/%{name}.php
%{_libdir}/%{name}/helper.php
%{_bindir}/%{name}
%doc config.sample.json


%changelog
* Wed Sep 19 2012 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-1.vortex
- Initial packageing.

