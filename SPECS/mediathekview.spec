%define __jar_repack %{nil}
%global debug_package %{nil}
%define mediathekview_home /opt/mediathekview
%define mediathekview_version 13.2.1
%define mediathekview_release fc29

Summary:    Application to download from German-speaking public broadcasting services online services
Name:       mediathekview
Version:    %{mediathekview_version}
BuildArch:  x86_64
Release:    %{mediathekview_release}
License:    GPLv3
URL:        https://mediathekview.de
Source0:    MediathekView-%{version}.tar.gz
Source1:    %{name}.desktop
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
    
BuildRequires:  desktop-file-utils

%description
Application to download from German-speaking public broadcasting services online services.

%prep
%setup -q -n MediathekView-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{mediathekview_home}/
cp -R * %{buildroot}/%{mediathekview_home}/

# Remove useless executable files
rm -f %{buildroot}/%{mediathekview_home}/*.command
rm -f %{buildroot}/%{mediathekview_home}/*.exe
rm -f %{buildroot}/%{mediathekview_home}/bin/*.exe
rm -f %{buildroot}/%{mediathekview_home}/bin/*.bat
rm -f %{buildroot}/%{mediathekview_home}/bin/*macosx**

# Desktop file
install -p -m 644 %_sourcedir/%{name}.desktop %{buildroot}/%{mediathekview_home}/%{name}.desktop

desktop-file-validate %{buildroot}/%{mediathekview_home}/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0775)
%{mediathekview_home}
%attr(0777,root,root) %{mediathekview_home}/*.sh
%attr(0777,root,root) %{mediathekview_home}/bin/*.sh
%attr(0644,root,root) %{mediathekview_home}/mediathekview.desktop
