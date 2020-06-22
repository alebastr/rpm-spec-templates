%global date    _
%global commit  _

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global distprefix  %{?date:.%{date}git%{shortcommit}}


Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.47

%description
%{summary}.


%prep
%autosetup -n %{name}-%{commit}


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
