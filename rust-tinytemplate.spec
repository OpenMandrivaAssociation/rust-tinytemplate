# Generated by rust2rpm 13
# Circular with criterion
%bcond_with check
%global debug_package %{nil}

%global crate tinytemplate

Name:           rust-%{crate}
Version:        1.0.3
Release:        2%{?dist}
Summary:        Simple, lightweight template engine

# Upstream license specification: Apache-2.0 OR MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/tinytemplate
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple, lightweight template engine.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
find . -executable -type f -exec chmod 0644 "{}" \;

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Josh Stone <jistone@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 17:57:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Release 1.0.2

* Wed Mar 20 09:47:28 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Run tests in infrastructure

* Fri Mar 08 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Initial package
