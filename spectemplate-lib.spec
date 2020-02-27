%global abi_ver 0

Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:  
Requires:       

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


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license add-license-file-here
%doc add-main-docs-here
%{_libdir}/*.so.%{abi_ver}*

%files devel
%doc add-devel-docs-here
%{_includedir}/*
%{_libdir}/*.so


%changelog
