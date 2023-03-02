Summary:	Bitstream 75dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 75dpi Bitstream
Name:		xorg-font-font-bitstream-75dpi
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-bitstream-75dpi-%{version}.tar.xz
# Source0-md5:	95e0bbf17b362686c2bdadafe1b4ac08
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/75dpi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitstream 75dpi bitmap fonts: Charter and Terminal.

%description -l pl.UTF-8
Fonty bitmapowe 75dpi Bitstream: Charter i Terminal.

%prep
%setup -q -n font-bitstream-75dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/75dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 75dpi

%postun
fontpostinst 75dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/75dpi/char*.pcf.gz
%{_fontsdir}/75dpi/tech*.pcf.gz
%{_fontsdir}/75dpi/term*.pcf.gz
