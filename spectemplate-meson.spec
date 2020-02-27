Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.47

%description
%{summary}.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
