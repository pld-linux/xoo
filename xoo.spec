#
Summary:	Wrapper around Xnest or Xepyhr for embedded emulation
Name:		xoo
Version:	0.7
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://projects.o-hand.com/sources/xoo/%{name}-%{version}.tar.gz
# Source0-md5:	9b1911cff0290be0f6eb1f8ba62dcbae
URL:		http://projects.o-hand.com/xoo/
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper around Xnest or Xepyhr for embedded emulation.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO README
%attr(755,root,root) %{_bindir}/xoo
%{_desktopdir}/xoo.desktop
%{_pixmapsdir}/xoo.png
%{_datadir}/xoo/
