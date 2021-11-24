%define oname settings

Name:           cutefish-settings
Version:        0.5
Release:        1
Summary:        System Settings application for Cutefish Desktop
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cutefishos/settings
Source:         https://github.com/cutefishos/settings/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5ModemManagerQt)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(libcrypt)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
Requires:       fishui

%description
Cutefish Settings - The System Settings application for Cutefish Desktop.

%prep
%autosetup -n %{oname}-%{version} -p1
#sed -i 's/\(Name=\)\(Settings\)/\1Cutefish \2/' %{oname}.desktop
sed -i 's/QApt/#QApt/' CMakeLists.txt
rm -rf src/update

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
