%define		php_name	php%{?php_suffix}
%define		modname	syck
%define		status		beta
Summary:	%{modname} - YAML-1.0 parser and emitter
Summary(pl.UTF-8):	%{modname} - analizator i emiter YAML-1.0
Name:		%{php_name}-pecl-%{modname}
Version:	0.9.3
Release:	1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	cbbe638b431f74eec71c76588cd14f7e
URL:		http://pecl.php.net/package/syck/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
BuildRequires:	syck-devel
%{?requires_php_extension}
Requires:	%{php_name}-hash
Requires:	php(core) >= 5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A binding to the Syck library.

YAML(tm) (rhymes with "camel") is a straightforward machine parsable
data serialization format designed for human readability and
interaction with scripting languages. YAML is optimized for data
serialization, configuration settings, log files, Internet messaging
and filtering.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Dowiązania do biblioteki Syck.

YAML(tm) (rymuje się ze słowem "camel") to prosty do analizy format
serializacji danych zaprojektowany pod kątem czytelności dla człowieka
i interakcji z językami skryptowymi. YAML jest zoptymalizowany pod
kątem wykorzystania w celu serializacji danych, przechowywania opcji
konfiguracyjnych, logów, komunikatorów internetowych czy różnorakich
filtrów.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	EXTENSION_DIR=%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CHANGELOG TODO
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
