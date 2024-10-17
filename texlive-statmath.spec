Name:		texlive-statmath
Version:	46925
Release:	2
Summary:	A LaTeX package for simple use of statistical notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/statmath
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers anumber of notational conventions to be used
in applied and theoretical papers in statistics which are
currently lacking in the popular amsmath package. The seasoned
LaTeX user will see that the provided commands are simple,
almost trivial, but will hopefully offer less cluttered
preambles as well as a welcome help for novice users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/statmath
%{_texmfdistdir}/tex/latex/statmath
%doc %{_texmfdistdir}/doc/latex/statmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
