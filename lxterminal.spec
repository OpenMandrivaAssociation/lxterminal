Summary:	Lightweight VTE-based terminal emulator
Name:		lxterminal
Version:	0.3.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	https://sourceforge.net/projects/lxde/files/LXTerminal%20%28terminal%20emulator%29/LXTerminal%20%{version}/%{name}-%{version}.tar.xz
Patch2:		mdk-lxterminal-conf.patch
BuildRequires:	intltool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	docbook-to-man
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
Requires:	termcap

%description
Desktop-independent VTE-based terminal emulator without any unnecessary
dependencies.
 
Feature:
* Support Multi-tab.
* It doesn't have any unnecessary dependencies.
* All instances share the same process to reduce memory usage.
* It has correct behavior with nice performance when resizing window,
  tab and VTE stuff.
* Using unix-socket instead of D-bus to accomplish all instances share
  the same process.

%prep
%setup -qn %{name}-%{version}
%patch2 -p0 -b.conf

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*x*/apps/lxterminal.png
%{_mandir}/man1/*

