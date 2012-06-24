Summary:	Dependency sort tool for ocaml sources
Summary(pl):	Program do sortowania zale�no�ci dla ocamla
Name:		ocamldsort
Version:	0.14.3
Release:	3
License:	GPL
Group:		Libraries
Source0:	ftp://quatramaran.ens.fr/pub/ara/ocamldsort/%{name}-%{version}.tar.gz
# Source0-md5:	1d17aad629dc8c5986929f373ff64238
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-camlp4 >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ocamldsort command scans a set of Objective Caml source files (.ml
and .mli files), sorts them according to their dependencies and prints
the sorted files in order to link their corresponding .cmo and .cmi
files. ocamldsort can be used to compile and link simple projects with
one command.

However for larger projects where separate compilation is desirable,
ocamldsort can also be used from within a makefile. See the README
file for a typical makefile.

%description -l pl
Komenda ocamldsort skanuje a nast�pnie sortuje zbi�r plik�w �r�d�owych
Ocamla (.ml i .mli). Sortowanie odbywa si� z uwzgl�dnieniem zachowania
zale�no�ci mi�dzy plikami. Posortowane nazwy plik�w wypisywane s� w
kolejno�ci umo�liwiaj�cej ich �atwe skonsolidowanie. ocamldsort mo�e
by� u�ywane do kompilacji prostych projekt�w jako tak zwany
jednolinijkowiec, ale jest on r�wnie� bardzo przydatny przy budowaniu
bardziej skomplikowanych projekt�w korzystaj�cych z Makefile itp.
Bardziej zaawansowane przyk�ady znajduj� si� w pliku readme.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ocamldsort.opt		${RPM_BUILD_ROOT}%{_bindir}/ocamldsort
install ocamldsort.1		${RPM_BUILD_ROOT}%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
