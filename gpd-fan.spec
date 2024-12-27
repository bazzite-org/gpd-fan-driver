%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     gpd-fan
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Driver to control fans on various GPD devices
License:  GPLv2
URL:      https://github.com/Cryolitia/gpd-fan-driver

Source0:  LICENSE

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Driver to control fans on various GPD devices

%build
install -D -m 0644 %{SOURCE0} %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE

%files
%license LICENSE

%changelog
{{{ git_dir_changelog }}}
