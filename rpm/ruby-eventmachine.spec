#
# spec file for package rubygem-eventmachine (Version 0.12.10)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           rubygem-eventmachine
Version:        0.12.10
Release:        1
%define mod_name eventmachine
#
Group:          Development/Languages/Ruby
License:        GPL
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
BuildRequires:  gcc-c++ openssl-devel pkg-config
Requires:       rubygems >= 1.3.5
#
Url:            http://rubyeventmachine.com/
#               http://rubyforge.org/projects/eventmachine
Source:         %{mod_name}-%{version}.gem
Source1:        rubygem-eventmachine.rpmlintrc
#
Summary:        Ruby/EventMachine socket engine library
%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%prep
%build
%install
%gem_install %{S:0}
%gem_cleanup

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
