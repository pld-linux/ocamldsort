Summary:	Dependency sort tool for ocaml sources
Summary(pl):	Program do sortowania zaleznosci dla ocamla
Name:		ocamldsort
Version:	0.14.3
Release:	1
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
one command

However for larger projects where separate compilation is desirable,
ocamldsort can also be used from within a makefile. See the README
file for a typical makefile.


%description -l pl
Komenda ocamldsort skanuje a nastepnie sortuje zbior plikow zrodlowych
Ocamla (.ml i .mli). Sortowanie odbywa sie z uwzglednieniem zachowanie
zaleznosci miedzy plikami. Posortowane nazwy plikow drukowane sa w
kolejnosci umoziwiajacej ich latwe zlinkowanie. ocamldsort moze byc
uzywane do kompilacji prostych projektow jako tak zwany
jednolinikowiec, ale jest on rowniez bardzo przydatny przy budowaniu
bardziej skomplikowanych projektow Makefile i takie tam. Zajrzyj do
pliku readme po bardziej zaawansowane przyklady.

%prep
%setup -q

%build
./configure --prefix=${RPM_BUILD_ROOT}%{_prefix} \
	    --mandir=${RPM_BUILD_ROOT}%{_mandir}

%{__make} CC="%{__cc} %{rpmcflags} -fPIC" opt

%install
rm -rf $RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_bindir}
install ocamldsort.opt ${RPM_BUILD_ROOT}%{_bindir}/ocamldsort

install -d ${RPM_BUILD_ROOT}%{_mandir}/man1/
install ocamldsort.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes THANKS
%attr(755,root,root) %{_bindir}
%attr(755,root,root) %{_mandir}
