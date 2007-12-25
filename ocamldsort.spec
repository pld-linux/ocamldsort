Summary:	Dependency sort tool for ocaml sources
Summary(pl.UTF-8):	Program do sortowania zależności dla ocamla
Name:		ocamldsort
Version:	0.14.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://quatramaran.ens.fr/pub/ara/ocamldsort/%{name}-%{version}.tar.gz
# Source0-md5:	9651d6afb204c0b22cd69be8a847e1d4
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

%description -l pl.UTF-8
Komenda ocamldsort skanuje a następnie sortuje zbiór plików źródłowych
Ocamla (.ml i .mli). Sortowanie odbywa się z uwzględnieniem zachowania
zależności między plikami. Posortowane nazwy plików wypisywane są w
kolejności umożliwiającej ich łatwe skonsolidowanie. ocamldsort może
być używane do kompilacji prostych projektów jako tak zwany
jednolinijkowiec, ale jest on również bardzo przydatny przy budowaniu
bardziej skomplikowanych projektów korzystających z Makefile itp.
Bardziej zaawansowane przykłady znajdują się w pliku readme.

%prep
%setup -q

%build
%configure
%{__make} -j1

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
