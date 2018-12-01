%define __jar_repack %{nil}
%global debug_package %{nil}
%define mediathekview_home /opt/mediathekview
%define mediathekview_version 13.2.1
%define mediathekview_release fc29

Summary:    MeidathekView
Name:       mediathekview
Version:    %{mediathekview_version}
BuildArch:  x86_64
Release:    %{mediathekview_release}
License:    GPLv3
URL:        https://mediathekview.de
Source0:    MediathekView-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
MediathekView is an application to search, watch and download shows from online service from Germanys public broadcasting services.

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

%clean
rm -rf %{buildroot}

#%pre

%files
%defattr(-,root,root,0775)
%{mediathekview_home}
%attr(0777,root,root) %{mediathekview_home}/*.sh
%attr(0777,root,root) %{mediathekview_home}/bin/*.sh

#%post
