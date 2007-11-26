%define		_modname	syck
%define		_status		beta
Summary:	%{_modname} - YAML-1.0 parser and emitter
Summary(pl.UTF-8):	%{_modname} - parser i emiter YAML-1.0	
Name:		php-pecl-%{_modname}
Version:	0.9.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	39db9d4c56407b59b7e9bbf7b7d53308
URL:		http://pecl.php.net/package/syck/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
BuildRequires:	syck-devel
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A binding to the Syck library.

YAML(tm) (rhymes with "camel") is a straightforward machine parsable
data serialization format designed for human readability and
interaction with scripting languages. YAML is optimized for data
serialization, configuration settings, log files, Internet messaging
and filtering.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Dowi�zania do biblioteki Syck.

YAML(tm) (rymuje si� ze s�owem "camel") to prosty do parsowania format
serializacji danych zaprojektowany pod katem czytelno�ci dla cz�owieka
i interakcji z j�zykami skryptowymi. YAML jest zoptymalizowany pod
k�tem wykorzystania w celu serializacji danych, przechowywania opcji
konfiguracyjnych, log�w, komunikator�w internetowych czy r�norakich
filtr�w.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d

%{__make} install \
	-C %{_modname}-%{version} \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	EXTENSION_DIR=%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CHANGELOG,TODO}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so