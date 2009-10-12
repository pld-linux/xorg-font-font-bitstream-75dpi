Summary:	Bitstream 75dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 75dpi Bitstream
Name:		xorg-font-font-bitstream-75dpi
Version:	1.0.1
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-bitstream-75dpi-%{version}.tar.bz2
# Source0-md5:	aed54fb53d2d24aff10c92985286d1e5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
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
	--build=%{_host_platform} \
	--host=%{_host_platform} \
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
%doc COPYING ChangeLog
%{_fontsdir}/75dpi/char*.pcf.gz
%{_fontsdir}/75dpi/tech*.pcf.gz
%{_fontsdir}/75dpi/term*.pcf.gz
