#
# Conditional build:
%bcond_with	gtkhtml		# gtkhtml bindings (broken)
#
%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl
#
Summary:	.NET language bindings for GNOME
Summary(pl.UTF-8):	Wiązania GNOME dla .NET
Name:		dotnet-gnome-sharp
Version:	2.16.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.16/gnome-sharp-%{version}.tar.bz2
# Source0-md5:	09034669acec52f9d9818d9a31c032d5
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-mint.patch
Patch2:		%{name}-automake.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.0
BuildRequires:	gnome-panel-devel >= 2.15.91
%{?with_gtkhtml:BuildRequires:	gtkhtml-devel >= 3.11.92}
BuildRequires:	libart_lgpl-devel >= 2.2.0
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	librsvg-devel >= 1:2.15.90
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	rpm-perlprov
BuildRequires:	vte-devel >= 0.13.6
Obsoletes:	dotnet-gtk-sharp2-gnome
Obsoletes:	gtk-sharp2
Requires:	gnome-panel-libs >= 2.15.91
Requires:	gnome-vfs2-libs >= 2.15.92
%{?with_gtkhtml:Requires:	gtkhtml >= 3.11.92}
Requires:	libart_lgpl >= 2.2.0
Requires:	librsvg >= 1:2.15.90
Requires:	mono >= 1.1.16.1
Requires:	vte >= 0.13.6
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GNOME libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z GNOME.

%package devel
Summary:	Development part of GNOME#
Summary(pl.UTF-8):	Część dla programistów GNOME#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc
Requires:	which
Obsoletes:	dotnet-gtk-sharp2-gnome-devel
Obsoletes:	gtk-sharp2-devel

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GNOME#.

%description devel -l pl.UTF-8
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z GNOME#.

%package static
Summary:	Static gtk-sharp libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtk-sharp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	dotnet-gtk-sharp2-gnome-static

%description static
Static gnome-sharp libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gnome-sharp.

%prep
%setup -q -n gnome-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp2-schemagen
%attr(755,root,root) %{_libdir}/libgnomesharpglue-2.so
%attr(755,root,root) %{_libdir}/libvtesharpglue-2.so
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_libdir}/libgnomesharpglue-2.la
%{_libdir}/libvtesharpglue-2.la
%{_prefix}/lib/mono/gac/art-sharp
%{_prefix}/lib/mono/gac/gconf-sharp
%{_prefix}/lib/mono/gac/gconf-sharp-peditors
%{_prefix}/lib/mono/gac/gnome-sharp
%{_prefix}/lib/mono/gac/gnome-vfs-sharp
%{?with_gtkhtml:%{_prefix}/lib/mono/gac/gtkhtml-sharp}
%{_prefix}/lib/mono/gac/rsvg-sharp
%{_prefix}/lib/mono/gac/vte-sharp

%{_prefix}/lib/mono/gac/policy.2.4.art-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.4.gnome-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gnome-vfs-sharp
%{?with_gtkhtml:%{_prefix}/lib/mono/gac/policy.2.4.gtkhtml-sharp}
%{_prefix}/lib/mono/gac/policy.2.4.rsvg-sharp
%{_prefix}/lib/mono/gac/policy.2.4.vte-sharp

%{_prefix}/lib/mono/gac/policy.2.6.art-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.6.gnome-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gnome-vfs-sharp
%{?with_gtkhtml:%{_prefix}/lib/mono/gac/policy.2.6.gtkhtml-sharp}
%{_prefix}/lib/mono/gac/policy.2.6.rsvg-sharp
%{_prefix}/lib/mono/gac/policy.2.6.vte-sharp

%{_prefix}/lib/mono/gac/policy.2.8.art-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.8.gnome-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gnome-vfs-sharp
%{?with_gtkhtml:%{_prefix}/lib/mono/gac/policy.2.8.gtkhtml-sharp}
%{_prefix}/lib/mono/gac/policy.2.8.rsvg-sharp
%{_prefix}/lib/mono/gac/policy.2.8.vte-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gnome-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/gnome-vfs-sharp.dll
%{?with_gtkhtml:%{_prefix}/lib/mono/gtk-sharp-2.0/gtkhtml-sharp.dll}
%{_prefix}/lib/mono/gtk-sharp-2.0/rsvg-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/vte-sharp.dll

%{_datadir}/gapi-2.0/art-api.xml
%{_datadir}/gapi-2.0/gnome-api.xml
%{_datadir}/gapi-2.0/gnome-vfs-api.xml
%{?with_gtkhtml:%{_datadir}/gapi-2.0/gtkhtml-api.xml}
%{_datadir}/gapi-2.0/rsvg-api.xml
%{_datadir}/gapi-2.0/vte-api.xml

%{_examplesdir}/%{name}-%{version}
%{_pkgconfigdir}/art-sharp-2.0.pc
%{_pkgconfigdir}/gconf-sharp-2.0.pc
%{_pkgconfigdir}/gnome-sharp-2.0.pc
%{_pkgconfigdir}/gnome-vfs-sharp-2.0.pc
%{?with_gtkhtml:%{_pkgconfigdir}/gtkhtml-sharp-2.0.pc}
%{_pkgconfigdir}/rsvg-sharp-2.0.pc
%{_pkgconfigdir}/vte-sharp-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomesharpglue-2.a
%{_libdir}/libvtesharpglue-2.a
