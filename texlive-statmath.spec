%global tl_name statmath
%global tl_revision 46925

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A LaTeX package for simple use of statistical notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/statmath
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/statmath.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers anumber of notational conventions to be used in
applied and theoretical papers in statistics which are currently lacking
in the popular amsmath package. The seasoned LaTeX user will see that
the provided commands are simple, almost trivial, but will hopefully
offer less cluttered preambles as well as a welcome help for novice
users.

