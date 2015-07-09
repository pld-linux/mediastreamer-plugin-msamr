#
# Conditional build:
%bcond_with	wb	# use AMR wideband instead of narrowband
#
Summary:	AMR audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku AMR dla mediastreamera
Name:		mediastreamer-plugin-msamr
Version:	0.0.2
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://download-mirror.savannah.gnu.org/releases/linphone/plugins/sources/msamr-%{version}.tar.gz
# Source0-md5:	98b9a0d5f55952b9e0ec6e99d64d7698
URL:		https://github.com/Distrotech/msamr
BuildRequires:	ortp-devel >= 0.16.0
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	opencore-amr-devel >= 0.1.2
BuildRequires:	pkgconfig
%{?with_wb:BuildRequires:	vo-amrwbenc-devel >= 0.1.1}
Requires:	mediastreamer >= 2.0.0
Requires:	opencore-amr >= 0.1.2
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
