%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6NewStuff
%define devname %mklibname KF6NewStuff -d
#define git 20240217

Name: kf6-knewstuff
Version: 6.15.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/knewstuff/-/archive/master/knewstuff-master.tar.bz2#/knewstuff-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/knewstuff-%{version}.tar.xz
%endif
Summary: Framework for downloading and sharing additional application data
URL: https://invent.kde.org/frameworks/knewstuff
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Attica)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Syndication)
Requires: %{libname} = %{EVRD}

%description
Framework for downloading and sharing additional application data

%package -n %{libname}
Summary: Framework for downloading and sharing additional application data
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Framework for downloading and sharing additional application data

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Framework for downloading and sharing additional application data

%prep
%autosetup -p1 -n knewstuff-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/knewstuff.*
%{_bindir}/knewstuff-dialog6
%{_datadir}/applications/org.kde.knewstuff-dialog6.desktop

%files -n %{devname}
%{_includedir}/KF6/KNewStuff
%{_includedir}/KF6/KNewStuffCore
%{_includedir}/KF6/KNewStuffWidgets
%{_libdir}/cmake/KF6NewStuff
%{_libdir}/cmake/KF6NewStuffCore

%files -n %{libname}
%{_libdir}/libKF6NewStuffCore.so*
%{_libdir}/libKF6NewStuffWidgets.so*
%{_qtdir}/qml/org/kde/newstuff

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/knewstuff6widgets.so
