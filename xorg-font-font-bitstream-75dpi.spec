# $Rev: 3201 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-bitstream-75dpi
Summary(pl):	font-bitstream-75dpi
Name:		xorg-font-font-bitstream-75dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bitstream-75dpi-%{version}.tar.bz2
# Source0-md5:	7088317a724555929b9ca4ca7e50a1f1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-bitstream-75dpi-%{version}-root-%(id -u -n)

%description
font-bitstream-75dpi

%description -l pl
font-bitstream-75dpi


%prep
%setup -q -n font-bitstream-75dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%{_libdir}/X11/fonts/75dpi/*
