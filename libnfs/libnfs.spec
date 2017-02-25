Name:		libnfs
Version:	1.9.8
Release:	2%{?dist}
Summary:	Client library for accessing NFS shares over a network
# The library is licensed as LGPLv2+, the protocol definition is BSD
License:	LGPLv2+ and BSD
URL:		https://github.com/sahlberg/libnfs
Source0:	https://sites.google.com/site/libnfstarballs/li/libnfs-%{version}.tar.gz

BuildRequires:	pkgconfig

%description
The libnfs package contains a library of functions for accessing NFSv2
and NFSv3 servers from user space. It provides a low-level, asynchronous
RPC library for accessing NFS protocols, an asynchronous library with
POSIX-like VFS functions, and a synchronous library with POSIX-like VFS
functions.


%package devel
Summary:	Development files for libnfs
# The library is licensed as LGPLv2+, the protocol definition is BSD
# and the example source code is GPLv3+.
License:	LGPLv2+ and BSD and GPLv3+

Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libnfs-devel package contains libraries and header files for
developing applications that use libnfs.


%package utils
Summary:	Utilities for accessing NFS servers
License:	GPLv3+

Requires:	%{name}%{?_isa} = %{version}-%{release}

%description utils
The libnfs-utils package contains simple client programs for accessing
NFS servers using libnfs.


%prep
%setup -q

%build
%configure --disable-static --disable-examples
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libnfs.so.*
%doc README
%license COPYING
%license LICENCE-*.txt

%files devel
%{_libdir}/libnfs.so
%{_includedir}/nfsc/
%{_libdir}/pkgconfig/libnfs.pc
%doc examples/*.c

%files utils
%{_bindir}/nfs-*
%{_mandir}/man1/nfs-*.1*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Ross Lagerwall <rosslagerwall@gmail.com> 1.9.8-1
- Bump to 1.9.8.
- Include examples and licence terms.

* Sun Mar 29 2015 Ross Lagerwall <rosslagerwall@gmail.com> 1.9.7-2
- Update packaging after review.

* Sun Mar 01 2015 Ross Lagerwall <rosslagerwall@gmail.com> 1.9.7-1
- Initial packaging
