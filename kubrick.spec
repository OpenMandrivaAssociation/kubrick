Name:		kubrick
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Game based on Rubik's Cube
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kubrick/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Kubrick is a game based on the Rubik's Cube™ puzzle.

The cube sizes range from 2x2x2 up to 6x6x6, or you can play with irregular
"bricks" such as 5x3x2 or "mats" such as 6x4x1 or 2x2x1. The game has a
selection of puzzles at several levels of difficulty, as well as demos of
pretty patterns and solution moves, or you can make up your own puzzles.

%files
%{_kde_bindir}/kubrick
%{_kde_applicationsdir}/kubrick.desktop
%{_kde_appsdir}/kubrick
%{_kde_docdir}/*/*/kubrick
%{_kde_iconsdir}/hicolor/*/apps/kubrick.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

