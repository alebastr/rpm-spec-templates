# template for binary from github built with CMake
Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.13
BuildRequires:  gcc-c++
BuildRequires:  make

%description
%{summary}.


%prep
%autosetup


# https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/
%build
%cmake -S . -B %{_vpath_builddir}
%make_build -C %{_vpath_builddir}


%install
%make_install -C %{_vpath_builddir}

%check
pushd %{_vpath_builddir}
ctest
popd

%files
%license LICENSE 
%doc README.md
%{_bindir}/%{name}


%changelog
