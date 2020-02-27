# template for library from github built with CMake

# Shared library version
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_listing_shared_library_files
%global abi_ver 0

Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  make

%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
%build
%cmake .
%make_build


%install
%make_install

# split files between base and -devel packages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_devel_packages
%files
%license LICENSE 
%doc README.md
%{_libdir}/*.so.%{abi_ver}*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
# Fedora discourages usage and packaging of static libraries
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#packaging-static-libraries
%exclude %{_libdir}/*.a


%changelog
