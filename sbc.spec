Summary:	SBC codec library
Summary(pl.UTF-8):	Biblioteka kodeka SBC
Name:		sbc
Version:	1.5
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	https://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
# Source0-md5:	6ff244dde9e5e12b26362a47ed91d3f9
Patch0:		non-x86.patch
URL:		http://www.bluez.org/
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBC (Bluetooth low-complexity, subband codec) library.

%description -l pl.UTF-8
Biblioteka SBC (kodeka Bluetooth o małej złożoności).

%package devel
Summary:	Header files for SBC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SBC
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SBC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SBC.

%package static
Summary:	Static SBC library
Summary(pl.UTF-8):	Statyczna biblioteka SBC
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SBC library.

%description static -l pl.UTF-8
Statyczna biblioteka SBC.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/sbcdec
%attr(755,root,root) %{_bindir}/sbcenc
%attr(755,root,root) %{_bindir}/sbcinfo
%attr(755,root,root) %{_libdir}/libsbc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsbc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsbc.so
%{_includedir}/sbc
%{_pkgconfigdir}/sbc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsbc.a
