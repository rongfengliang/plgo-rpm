Name: plgo-rpm
Version: 1.0
Release: 1%{?dist}
Summary: this is a postgresql extension  with plgo dev
License: APACHE
URL:  https://github.com/rongfengliang/plgo-rpm
Source: https://github.com/rongfengliang/plgo-rpm/archive/v1.0.zip
%prep
%setup -q

%description
this is a postgresql extension  with plgo dev

%install
%{make_install} PREFIX=%{_prefix}

%files
/usr/pgsql-10/share/extension/example--0.1.sql
/usr/pgsql-10/share/extension/example.control
/usr/pgsql-10/lib/example.so
