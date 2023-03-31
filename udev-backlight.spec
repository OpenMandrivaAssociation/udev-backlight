Name: udev-backlight
Version: 0.1
Release: 2
Summary: Udev rules for setting permissions on backlight devices
URL: https://openmandriva.org/
License: GPLv3
Group: Hardware
BuildArch: noarch

%description
Udev rules for setting permissions on backlight devices

%prep

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
cat >%{buildroot}%{_prefix}/lib/udev/rules.d/80-backlight.rules <<'EOF'
ACTION=="add", SUBSYSTEM=="backlight", KERNEL=="acpi_video0", GROUP="video", MODE="0664"
EOF


%files
%{_prefix}/lib/udev/rules.d/80-backlight.rules
