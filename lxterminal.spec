# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		116f89f71769b9a9852845f9308f73ba5de26bff
	%global commitdate	20241210
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Lightweight VTE-based terminal emulator
Name:		lxterminal
Version:	0.4.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.sourceforge.net/
#Source0:	https://sourceforge.net/projects/lxde/files/LXTerminal%20%28terminal%20emulator%29/LXTerminal%20%{version}/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxterminal/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
Patch100:	lxterminal-openmandriva_conf.patch
BuildRequires:	intltool
#BuildRequires: pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.91)
BuildRequires:	pkgconfig(libpcre2-32)
BuildRequires:	docbook-to-man
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
Requires:	termcap

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/*

#---------------------------------------------------------------------------

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
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	-enable-gtk3
%make_build

%install
%make_install

# locales
%find_lang %{name}

