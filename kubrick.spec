%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Game based on Rubik's Cube
Name:		kubrick
Version:	 17.12.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kubrick/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake ninja cmake(ECM)
BuildRequires:	cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5I18n) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5OpenGL) cmake(Qt5Svg) cmake(Qt5Widgets)

%description
Kubrick is a game based on the Rubik's Cube™ puzzle.

The cube sizes range from 2x2x2 up to 6x6x6, or you can play with irregular
"bricks" such as 5x3x2 or "mats" such as 6x4x1 or 2x2x1. The game has a
selection of puzzles at several levels of difficulty, as well as demos of
pretty patterns and solution moves, or you can make up your own puzzles.

%files -f %{name}.lang
%{_bindir}/kubrick
%{_datadir}/applications/org.kde.kubrick.desktop
%{_datadir}/kubrick
%{_datadir}/metainfo/*.xml
%{_iconsdir}/hicolor/*/apps/kubrick.png
%{_datadir}/kxmlgui5/kubrick

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
