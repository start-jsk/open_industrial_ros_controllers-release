Name:           ros-indigo-open-industrial-ros-controllers
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS open_industrial_ros_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/open_industrial_ros_controllers
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-open-controllers-interface
BuildRequires:  ros-indigo-catkin

%description
This package provides common functionality, especially plugin architecture for
industrial robot controllers, much like the one in pr2_mechanism. The plan is in
the near future to utilize or integrate with existing other controller packages.

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
* Fri Oct 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.0-0
- Autogenerated by Bloom

* Sat Mar 14 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.4-0
- Autogenerated by Bloom

