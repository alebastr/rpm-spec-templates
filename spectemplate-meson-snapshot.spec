%global gitdate  _
%global commit   _

%global scommit  %(c=%{commit}; echo ${c:0:7})
%global gitrel   %{?gitdate:.%{gitdate}git%{scommit}}
%global gitver   %{?gitdate:-%{gitdate}git%{scommit}}


Name:           
Version:        
Release:        1%{?gitrel}%{?dist}
Summary:        

License:        
URL:            https://github.com/{{author}}/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}%{?gitver}.tar.gz

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
