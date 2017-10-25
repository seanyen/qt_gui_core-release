Name:           ros-lunar-qt-dotgraph
Version:        0.3.7
Release:        0%{?dist}
Summary:        ROS qt_dotgraph package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_dotgraph
Source0:        %{name}-%{version}.tar.gz

Requires:       pydot
Requires:       ros-lunar-python-qt-binding >= 0.3.0
BuildRequires:  graphviz-python
BuildRequires:  ros-lunar-catkin

%description
qt_dotgraph provides helpers to work with dot graphs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Oct 25 2017 D. Hood <dhood@osrfoundation.org> - 0.3.7-0
- Autogenerated by Bloom

* Thu Aug 03 2017 D. Hood <dhood@osrfoundation.org> - 0.3.6-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.5-0
- Autogenerated by Bloom

* Wed Mar 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-2
- Autogenerated by Bloom

* Wed Mar 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-1
- Autogenerated by Bloom

* Fri Feb 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-0
- Autogenerated by Bloom

