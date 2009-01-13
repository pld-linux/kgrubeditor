#
%define		orgname		KGRUBEditor
%define		qt_ver		4.4.1

Summary:	KDE GRUB configuration module
Summary(pl.UTF-8):	Modul konfiguracji GRUB-a do KDE
Name:		kgrubeditor
Version:	0.8.5
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{orgname}-%{version}-src.tar.bz2
# Source0-md5:	c6d1fb21989f403276103887f344fdf3
URL:		http://artfowl.blogspot.com/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGRUBEditor is a KDE utility, that edits GRUB's configuration files
through an inituitive user interface. It combines both ease of use 
with flexibility and is the perfect solution for those who want to 
configure GRUB, without messing with its files.

# todo, i need to setup the polish keyboard first
#%description -l pl.UTF-8

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgrubeditor.so
%{_datadir}/apps/kgrubeditor
%{_datadir}/config.kcfg/kgrubeditor.kcfg
%{_datadir}/config/kgrubeditor_splash.knsrc
%{_datadir}/kde4/services/kgrubeditor.desktop
%{_desktopdir}/kde4/kgrubeditor_app.desktop
%{_iconsdir}/hicolor/*x*/apps/kgrubeditor.png
%{_iconsdir}/hicolor/scalable/apps/kgrubeditor.svgz
