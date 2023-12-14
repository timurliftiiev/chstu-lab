Name:           count-files
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to count files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/timurliftiiev/chstu-lab
Source0:        https://github.com/timurliftiiev/chstu-lab/archive/main.zip

BuildArch:      noarch

%description
count-files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd chstu-lab

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/chstu-lab/count-files.sh %{buildroot}/usr/bin/count-files

%files
/usr/bin/count-files

%changelog
* Thu Dec 14 2023 Timur Liftiiev <timur.liftiiev@gmail.com> - 1.0-1
- Initial build
