Name:           ros-indigo-qt-gui-app
Version:        0.2.33
Release:        0%{?dist}
Summary:        ROS qt_gui_app package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui_app
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-qt-gui
BuildRequires:  ros-indigo-catkin

%description
qt_gui_app provides the main to start an instance of the integrated graphical
user interface provided by qt_gui.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue May 22 2018 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.33-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.32-0
- Autogenerated by Bloom

* Wed Nov 02 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.31-0
- Autogenerated by Bloom

* Wed Mar 30 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.30-0
- Autogenerated by Bloom

* Sun Sep 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.29-0
- Autogenerated by Bloom

* Mon Jun 08 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.28-0
- Autogenerated by Bloom

* Sat May 02 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.27-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.26-0
- Autogenerated by Bloom

