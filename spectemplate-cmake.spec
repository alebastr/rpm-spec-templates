# template for binary from github built with CMake
%undefine       _cmake_in_source_build

Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
%{summary}.


%prep
%autosetup


# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE 
%doc README.md
%{_bindir}/%{name}


%changelog
