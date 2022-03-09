Name:		 libepoxy
Version:	 1.5.9
Release: 	 2
Summary:	 library work with epoxy runtime 
License:	 MIT
URL:		 https://github.com/anholt/%{name}
Source0:         https://github.com/anholt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz 

BuildRequires:   meson gcc libGL-devel libEGL-devel libX11-devel
BuildRequires:   python3 xorg-x11-server-Xvfb mesa-dri-drivers
BuildRequires:   pkgconfig(glesv2) pkgconfig(gl) pkgconfig(egl)
%ifarch riscv64
BuildRequires:   pkgconfig(x11) pkgconfig(xorg-macros)
%endif

%description
A library for handling OpenGL function pointer management.

%package	 devel
Summary:	 Development files for %{name}
Requires:	 %{name} = %{version}-%{release}
%ifarch riscv64
Requires:	 glibc-devel
Requires:	 pkgconfig(egl)
Requires:	 pkgconfig(x11)
%endif

%description 	 devel
%{name}-devel contains the header files for developing
applications that want to make use of %{name}.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1 

%build
%meson         \
%ifarch riscv64
 -D glx=no     \
 -D egl=yes    \
 -D x11=true   \
%endif
 %{nil}
%meson_build

%install
%meson_install

%check
xvfb-run -d -s "-screen 0 640x480x24" ninja -C %{_vpath_builddir} test || \
    (cat %{_vpath_builddir}/meson-logs/testlog.txt ; exit 1)

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/%{name}.so.0*

%files devel
%defattr(-,root,root)
%{_includedir}/epoxy/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/epoxy.pc

%files help
%defattr(-,root,root)
%doc README.md

%changelog
* Mon Mar 07 2022 Jingwiw <ixoote@gmail.com> - 1.5.9-2
- fix support for riscv64
- allow libopengl to be used when GLX_LIB is missing
- optimize requires for riscv64 about opengl and x11

* Thu Dec 02 2021 xingxing <xingxing9@huawei.com> - 1.5.9-1
- update to 1.5.9

* Fri Jan 29 2021 zhanzhimin <zhanzhimin@huawei.com> - 1.5.5-1
- update to 1.5.5

* Mon Aug 03 2020 orange-snn <songnannan2@huawei.com> - 1.5.4-2
- change the buildrequires form mesa to libglvnd

* Mon Jun 22 2020 xinghe<xinghe1@huawei.com> - 1.5.4-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update to 1.5.4

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.5.3-2
- Package init
