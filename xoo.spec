Summary:	Wrapper around Xnest or Xephyr for embedded emulation
Summary(pl.UTF-8):	Wrapper Xnest lub Xephyr do emulacji urządzeń wbudowanych
Name:		xoo
Version:	0.7
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://projects.o-hand.com/sources/xoo/%{name}-%{version}.tar.gz
# Source0-md5:	9b1911cff0290be0f6eb1f8ba62dcbae
URL:		http://projects.o-hand.com/xoo/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	expat-devel
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libglade2-devel >= 1:2.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper around Xnest or Xepyhr for embedded emulation.

%description -l pl.UTF-8
Wrapper Xnest lub Xephyr do emulacji urządzeń wbudowanych.

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
%{_datadir}/xoo
