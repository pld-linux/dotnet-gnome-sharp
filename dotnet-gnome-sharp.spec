#
# Conditional build:
%bcond_without	libart		# libart_lgpl binding
%bcond_without	gnomevfs	# gnome-vfs2 binding
%bcond_without	gnomeui		# gnome (libgnomecanvas+libgnomeui) binding
#
Summary:	GNOME# - .NET language bindings for GNOME libraries
Summary(pl.UTF-8):	GNOME# - wiązania .NET do bibliotek GNOME
Name:		dotnet-gnome-sharp
Version:	2.24.5
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-sharp/2.24/gnome-sharp-%{version}.tar.bz2
Source0:	http://download.mono-project.com/sources/gnome-sharp2/gnome-sharp-%{version}.tar.gz
# Source0-md5:	26be828348b0c6ef020f313b6f92fbba
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-mint.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
# gapi-2.0, gtk-sharp-2.0, glade-sharp-2.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.2
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.24.0}
%{?with_gnomeui:BuildRequires:	gtk+2-devel >= 2:2.14.0}
%{?with_libart:BuildRequires:	libart_lgpl-devel >= 2.3.20}
%{?with_gnomeui:BuildRequires:	libgnomecanvas-devel >= 2.20.0}
%{?with_gnomeui:BuildRequires:	libgnomeui-devel >= 2.24.0}
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 2.7
BuildRequires:	mono-devel >= 2.7
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	dotnet-art-sharp = %{version}-%{release}
Requires:	dotnet-gnome-vfs-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2 >= 2.12.2
Requires:	gtk+2 >= 2:2.14.0
Requires:	libgnomecanvas >= 2.20.0
Requires:	libgnomeui >= 2.24.0
Requires:	mono >= 2.7
Obsoletes:	dotnet-gtk-sharp2-gnome
Obsoletes:	gtk-sharp2
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GNOME libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z GNOME.

%package devel
Summary:	Development files for GNOME# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNOME#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-art-sharp-devel = %{version}-%{release}
Requires:	dotnet-gnome-vfs-sharp-devel = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.2
Requires:	monodoc
Requires:	which
Obsoletes:	dotnet-gtk-sharp2-gnome-devel
Obsoletes:	gtk-sharp2-devel

%description devel
Development files for GNOME# library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki GNOME#.

%package static
Summary:	Static GNOME# glue library
Summary(pl.UTF-8):	Statyczna biblioteka warstwy sklejającej GNOME#
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	dotnet-gtk-sharp2-gnome-static

%description static
Static GNOME# glue library.

%description static -l pl.UTF-8
Statyczna biblioteka warstwy sklejającej GNOME#.

%package examples
Summary:	Examples for GNOME# libraries
Summary(pl.UTF-8):	Przykłado do bibliotek GNOME#
Group:		Development/Libraries
Conflicts:	dotnet-gnome-sharp-devel < 2.24.2-4

%description examples
Examples for GNOME# libraries.

%description examples -l pl.UTF-8
Przykłady do bibliotek GNOME#.

%package -n dotnet-art-sharp
Summary:	Art# - .NET binding for libart library
Summary(pl.UTF-8):	Art# - wiązanie .NET do biblioteki libart
Group:		Libraries
Requires:	libart_lgpl >= 2.3.20
Requires:	mono >= 2.7
Conflicts:	dotnet-gnome-sharp < 2.24.2-4

%description -n dotnet-art-sharp
Art# - .NET binding for libart library.

%description -n dotnet-art-sharp -l pl.UTF-8
Art# - wiązanie .NET do biblioteki libart.

%package -n dotnet-art-sharp-devel
Summary:	Development files for Art# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Art#
Group:		Development/Libraries
Requires:	dotnet-art-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.2

%description -n dotnet-art-sharp-devel
Development files for Art# library.

%description -n dotnet-art-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki Art#.

%package -n dotnet-gconf-sharp
Summary:	GConf# - .NET binding for GConf 2 library
Summary(pl.UTF-8):	GConf# - wiązanie .NET do biblioteki GConf 2
Group:		Libraries
Requires:	GConf2-libs
Requires:	mono >= 2.7
Conflicts:	dotnet-gnome-sharp < 2.24.2-4

%description -n dotnet-gconf-sharp
GConf# - .NET binding for GConf 2 library.

%description -n dotnet-gconf-sharp -l pl.UTF-8
GConf# - wiązanie .NET do biblioteki GConf 2.

%package -n dotnet-gconf-sharp-devel
Summary:	Development files for GConf# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GConf#
Group:		Development/Libraries
Requires:	dotnet-gconf-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.2

%description -n dotnet-gconf-sharp-devel
Development files for GConf# library.

%description -n dotnet-gconf-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GConf#.

%package -n dotnet-gconf-sharp-peditors
Summary:	GConf# Property Editing classes
Summary(pl.UTF-8):	Klasy GConf# Property Editing
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gconf-sharp = %{version}-%{release}

%description -n dotnet-gconf-sharp-peditors
GConf.PropertyEditors# - GConf# Property Editing classes.

%description -n dotnet-gconf-sharp-peditors -l pl.UTF-8
GConf.PropertyEditors# - klasy GConf# Property Editing.

%package -n dotnet-gconf-sharp-peditors-devel
Summary:	Development files for GConf# Property Editing classes
Summary(pl.UTF-8):	Pliki programistyczne biblioteki klas GConf# Property Editing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	dotnet-gconf-sharp-devel = %{version}-%{release}
Requires:	dotnet-gconf-sharp-peditors = %{version}-%{release}

%description -n dotnet-gconf-sharp-peditors-devel
Development files for GConf# Property Editing classes.

%description -n dotnet-gconf-sharp-peditors-devel -l pl.UTF-8
Pliki programistyczne biblioteki klas GConf# Property Editing.

%package -n dotnet-gnome-vfs-sharp
Summary:	GnomeVfs# - .NET binding for GNOME-VFS 2 library
Summary(pl.UTF-8):	GnomeVfs# - wiązanie .NET do biblioteki GNOME-VFS 2
Group:		Libraries
Requires:	gnome-vfs2-libs >= 2.24.0
Requires:	mono >= 2.7
Conflicts:	dotnet-gnome-sharp < 2.24.2-4

%description -n dotnet-gnome-vfs-sharp
GnomeVfs# - .NET binding for GNOME-VFS 2 library.

%description -n dotnet-gnome-vfs-sharp -l pl.UTF-8
GnomeVfs# - wiązanie .NET do biblioteki GNOME-VFS 2.

%package -n dotnet-gnome-vfs-sharp-devel
Summary:	Development files for GnomeVfs# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GnomeVfs#
Group:		Development/Libraries
Requires:	dotnet-gnome-vfs-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.2

%description -n dotnet-gnome-vfs-sharp-devel
Development files for GnomeVfs# library.

%description -n dotnet-gnome-vfs-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GnomeVfs#.

%prep
%setup -q -n gnome-sharp-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%if %{with gnomeui}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomesharpglue-2.so
%{_libdir}/libgnomesharpglue-2.la
%{_prefix}/lib/mono/gac/gnome-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/gnome-sharp.dll
%{_datadir}/gapi-2.0/gnome-api.xml
%{_pkgconfigdir}/gnome-sharp-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomesharpglue-2.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with libart}
%files -n dotnet-art-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/art-sharp
%{_prefix}/lib/mono/gac/policy.2.4.art-sharp
%{_prefix}/lib/mono/gac/policy.2.6.art-sharp
%{_prefix}/lib/mono/gac/policy.2.8.art-sharp
%{_prefix}/lib/mono/gac/policy.2.16.art-sharp
%{_prefix}/lib/mono/gac/policy.2.20.art-sharp

%files -n dotnet-art-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.16.art-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.20.art-sharp.dll
%{_datadir}/gapi-2.0/art-api.xml
%{_pkgconfigdir}/art-sharp-2.0.pc
%endif

%files -n dotnet-gconf-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp2-schemagen
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_prefix}/lib/mono/gac/gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.16.gconf-sharp
%{_prefix}/lib/mono/gac/policy.2.20.gconf-sharp

%files -n dotnet-gconf-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.16.gconf-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.20.gconf-sharp.dll
%{_pkgconfigdir}/gconf-sharp-2.0.pc

%if %{with gnomeui}
%files -n dotnet-gconf-sharp-peditors
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.4.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.6.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.8.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.16.gconf-sharp-peditors
%{_prefix}/lib/mono/gac/policy.2.20.gconf-sharp-peditors

%files -n dotnet-gconf-sharp-peditors-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.16.gconf-sharp-peditors.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.20.gconf-sharp-peditors.dll
%{_pkgconfigdir}/gconf-sharp-peditors-2.0.pc
%endif

%if %{with gnomevfs}
%files -n dotnet-gnome-vfs-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gnome-vfs-sharp
%{_prefix}/lib/mono/gac/policy.2.4.gnome-vfs-sharp
%{_prefix}/lib/mono/gac/policy.2.6.gnome-vfs-sharp
%{_prefix}/lib/mono/gac/policy.2.8.gnome-vfs-sharp
%{_prefix}/lib/mono/gac/policy.2.16.gnome-vfs-sharp
%{_prefix}/lib/mono/gac/policy.2.20.gnome-vfs-sharp

%files -n dotnet-gnome-vfs-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtk-sharp-2.0/gnome-vfs-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.4.gnome-vfs-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.6.gnome-vfs-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.8.gnome-vfs-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.16.gnome-vfs-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-2.0/policy.2.20.gnome-vfs-sharp.dll
%{_datadir}/gapi-2.0/gnome-vfs-api.xml
%{_pkgconfigdir}/gnome-vfs-sharp-2.0.pc
%endif
