Summary:	Fraunhofer FDK AAC Codec library
Summary(pl.UTF-8):	Biblioteka kodeka Fraunhofer FDK AAC
Name:		fdk-aac
Version:	2.0.2
Release:	1
License:	distributable, patent license required in some countries
Group:		Libraries
Source0:	https://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz
# Source0-md5:	b41222194b31f570b3132bd622a9aef6
URL:		https://github.com/mstorsjo/fdk-aac
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is
software that implements the MPEG Advanced Audio Coding ("AAC")
encoding and decoding scheme for digital audio. This FDK AAC Codec
software is intended to be used on a wide variety of Android devices.

%description -l pl.UTF-8
Biblioteka kodeka Fraunhofer FDK AAC dla Androida ("FDK AAC Codec") to
oprogramowanie będące implementacją algorytmu kodowania i dekodowania
MPEG Advanced Audio Coding ("AAC") dla dźwięku cyfrowego. FDK AAC
Codec jest przeznaczony do użycia na rozmaitych urządzeniach typu
Android.

%package devel
Summary:	Header files for Fraunhofer FDK AAC Codec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki kodeka Fraunhofer FDK AAC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for Fraunhofer FDK AAC Codec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki kodeka Fraunhofer FDK AAC.

%package static
Summary:	Static Fraunhofer FDK AAC Codec library
Summary(pl.UTF-8):	Statyczna biblioteka kodeka Fraunhofer FDK AAC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Fraunhofer FDK AAC Codec library.

%description static -l pl.UTF-8
Statyczna biblioteka kodeka Fraunhofer FDK AAC.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no dependencies and pkg-config file present
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfdk-aac.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NOTICE
%attr(755,root,root) %{_libdir}/libfdk-aac.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfdk-aac.so.2

%files devel
%defattr(644,root,root,755)
%doc documentation/aac{Decoder,Encoder}.pdf
%attr(755,root,root) %{_libdir}/libfdk-aac.so
%{_includedir}/fdk-aac
%{_pkgconfigdir}/fdk-aac.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfdk-aac.a
