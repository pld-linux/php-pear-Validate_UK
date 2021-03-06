%define		_class		Validate
%define		_subclass	UK
%define		_status		alpha
%define		_pearname	Validate_UK

Summary:	%{_pearname} - Validation class for UK
Summary(pl.UTF-8):	%{_pearname} - Klasa walidacji dla Zjednoczonego Królestwa
Name:		php-pear-%{_pearname}
Version:	0.5.4
Release:	3
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8756ac18573c016196783a6ea75187f3
Source1:	%{name}-carReg.php
URL:		http://pear.php.net/package/Validate_UK/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Obsoletes:	php-pear-Validate_UK-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for UK such as:
 - SSN (National Insurance/IN)
 - Postal Code
 - Sort Code
 - Bank AC
 - Telephone numbers
 - Car registration numbers
 - Passports
 - Driver license

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet dostarcza metody do sprawdzania poprawności dla Zjednoczonego
Królestwa danych takich jak:
 - SSN (numer ubezpieczenia)
 - Kod pocztowy
 - Sort code
 - numer konta bankowego
 - numer telefonu
 - numer rejestracyjny samochodu
 - numer paszportu
 - numer prawa jazdy

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install
install -D %{SOURCE1} $RPM_BUILD_ROOT%{php_pear_dir}/Validate/UK/carReg.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/UK
%{php_pear_dir}/Validate/UK.php
