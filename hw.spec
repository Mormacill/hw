Name:       hw
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

BuildRequires: gcc

%description
This is my first RPM package, which does say Hello World.

%prep
curl https://raw.githubusercontent.com/Mormacill/coprtest/main/hw.c --output hw.c

%build
gcc hw.c

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 a.out %{buildroot}/usr/bin/a.out

%files
/usr/bin/a.out

%changelog
# let's skip this for now
