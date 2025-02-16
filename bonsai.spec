#define snapshot 20220107

Name:		bonsai
Version:	1.1.3
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Git repository manager for Plasma Mobile
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/bonsai/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTerminal4)
BuildRequires:	gettext
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	cmake(Qt6QuickCompiler)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

%description
Git repository manager for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang bonsai

%files -f bonsai.lang
%{_bindir}/bonsai
#{_libdir}/libGitWrap.so
%{_datadir}/applications/org.kde.bonsai.desktop
%{_datadir}/icons/hicolor/scalable/apps/bonsai.svg
%{_datadir}/metainfo/org.kde.bonsai.appdata.xml
