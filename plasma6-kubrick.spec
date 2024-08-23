#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Game based on Rubik's Cube
Name:		plasma6-kubrick
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kubrick/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kubrick/-/archive/%{gitbranch}/kubrick-%{gitbranchd}.tar.bz2#/kubrick-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kubrick-%{version}.tar.xz
%endif
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(OpenGL)
BuildRequires:	cmake(KF6DocTools)

%description
Kubrick is a game based on the Rubik's Cube™ puzzle.

The cube sizes range from 2x2x2 up to 6x6x6, or you can play with irregular
"bricks" such as 6x3x2 or "mats" such as 6x4x1 or 2x2x1. The game has a
selection of puzzles at several levels of difficulty, as well as demos of
pretty patterns and solution moves, or you can make up your own puzzles.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kubrick.renamecategories
%{_datadir}/qlogging-categories6/kubrick.categories
%{_bindir}/kubrick
%{_datadir}/applications/org.kde.kubrick.desktop
%{_datadir}/kubrick
%{_datadir}/metainfo/*.xml
%{_iconsdir}/hicolor/*/apps/kubrick.png

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kubrick-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
