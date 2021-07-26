#
# Conditional build:
%bcond_with	wb	# use AMR wideband instead of narrowband
#
Summary:	AMR audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku AMR dla mediastreamera
Name:		mediastreamer-plugin-msamr
Version:	1.1.3
Release:	3
License:	GPL v2+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/msamr/-/tags
#Source0:	https://gitlab.linphone.org/BC/public/msamr/-/archive/%{version}/msamr-%{version}.tar.bz2
Source0:	http://linphone.org/releases/old/sources/plugins/msamr/msamr-%{version}.tar.gz
# Source0-md5:	10c6a05e12c2af17f4ebc215d6c477da
URL:		https://gitlab.linphone.org/BC/public/msamr
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	ortp-devel >= 0.16.0
BuildRequires:	mediastreamer-devel >= 2.13.0
BuildRequires:	opencore-amr-devel >= 0.1.2
BuildRequires:	pkgconfig
%{?with_wb:BuildRequires:	vo-amrwbenc-devel >= 0.1.1}
Requires:	mediastreamer >= 2.13.0
Requires:	opencore-amr >= 0.1.2
Requires:	ortp >= 0.16.0
%{?with_wb:Requires:	vo-amrwbenc >= 0.1.1}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the AMR audio
codec.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka dźwięku AMR.

%prep
%setup -q -n msamr-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_wb:--enable-wideband}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmsamr.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsamr.so*
