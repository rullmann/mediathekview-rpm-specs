%define __jar_repack %{nil}
%global debug_package %{nil}
%define mediathekview_home /opt/mediathekview
%define mediathekview_version 13.3.0
%define mediathekview_release 1

%undefine _disable_source_fetch

Summary:       Application to download shows from German-speaking public broadcasting
Name:          mediathekview
Version:       %{mediathekview_version}
ExclusiveArch: x86_64
Release:       %{mediathekview_release}
License:       GPLv3
URL:           https://mediathekview.de
Source0:       https://download.mediathekview.de/stabil/MediathekView-13.3.0-linux.tar.gz
%define        SHA512SUM0 76455f4217c9a285455d86d79cc03afb11951060f9dbb1d1e3a29cce415de09e96963f1a637b26b157474b968741a68f5cb95f542916c791af64871d4ad6b62d
Source1:       %{name}.desktop
Source2:       MediathekView.sh
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{mediathekview_release}%{?dist}-root-%(%{__id_u} -n)

Requires:      java-11-openjdk
BuildRequires: desktop-file-utils

%description
Application to download shows from German-speaking public broadcasting.

%prep
%setup -q -c

%build

%install
install -d -m 755 %{buildroot}/%{mediathekview_home}/
cp -R * %{buildroot}/%{mediathekview_home}/

# Desktop file
install -d -m 755 %{buildroot}/%{_datadir}/applications/
install -p -m 644 %_sourcedir/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -p -m 755 %_sourcedir/MediathekView.sh %{buildroot}/%{mediathekview_home}/MediathekView.sh

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-install %{buildroot}/%{_datadir}/applications/%{name}.desktop --add-category="AudioVideo"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0775)
%{mediathekview_home}
%attr(0777,root,root) %{mediathekview_home}/*.sh
%attr(0777,root,root) %{mediathekview_home}/bin/*.sh
%attr(0644,root,root) %{_datadir}/applications/%{name}.desktop
