%global debug_package %{nil}
%global gitdate 20170210
%global gitversion 76b3da97b

Name:		virglrenderer
Version:	0.6.0
Release:	1.%{gitdate}git%{gitversion}%{?dist}

Summary:	Virgl Rendering library.
Group:		Applications/Emulators
License:	MIT

#VCS: git:git://anongit.freedesktop.org/git/virglrenderer
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:	virglrenderer-%{gitdate}.tar.xz

BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-x11-util-macros
BuildRequires:	libepoxy-devel
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libEGL-devel
BuildRequires:	python
BuildRequires:	libdrm-devel

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package devel
Summary: Virgil3D renderer development files
Group:	Applications/Emulators

Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server
Group:	Applications/Emulators

Requires: %{name}%{?_isa} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%setup -q -n %{name}-%{gitdate}
%build
sh autogen.sh
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" install
find %{buildroot} -type f -name '*.la' | xargs rm -f -- || :

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server

%changelog
* Fri Feb 10 2017 Dave Airlie <airlied@redhat.com> - 0.6.0-1.git
- upstream 0.6.0 release

* Mon Apr 11 2016 Dave Airlie <airlied@redhat.com> 0.5.0-1.git
- upstream 0.5.0 release

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> 0.4.1-1.git
- fix regression in last build

* Wed Feb 17 2016 Dave Airlie <airlied@redhat.com> 0.4.0-1.git
- latest git snapshot with new API

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3.20151215gite9d3c0c27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dave Airlie <airlied@redhat.com> 0.3.0-2.gite9d3c0c27
- latest upstream to fix gnome-shell rendering bugs

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.3.0-1.20151023git9ce005e5a
- update to latest upstream to fix shader issue

* Fri Oct 23 2015 Dave Airlie <airlied@redhat.com> 0.2.0-1.20151023git5bfba5190
- update to latest upstream

* Thu Jul 09 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150420gitc4fb40201.2
- fix FTBFS (#1240041)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.20150420gitc4fb40201.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dave Airlie <airlied@redhat.com> 0.0.1-0.20150401gita9ba2c442
- initial virglrenderer spec


