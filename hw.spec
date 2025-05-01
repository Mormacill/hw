Name:       hw
Version:    1.3
Release:    %autorelease
Summary:    Most simple RPM package
License:    FIXME
Source0: https://github.com/Mormacill/hw/archive/refs/tags/%{version}.tar.gz
BuildRequires: gcc

%description
This is my first RPM package, which does say Hello World.

%prep
%setup -q

%build
gcc -g -o hw hw.c

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hw %{buildroot}/usr/bin/hw

%files
/usr/bin/hw

%changelog
* Thu May 01 2025 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1.3-1
- Update hw.spec

* Thu May 01 2025 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1.2-1
- Update hw.spec

* Thu May 01 2025 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1.1-2
- Update hw.c

* Thu May 01 2025 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1.1-1
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-7
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-6
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-5
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-4
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-3
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-2
- Update hw.spec

* Mon Mar 21 2022 Mormacill <31103546+Mormacill@users.noreply.github.com> - 1-1
- Create hw.spec
