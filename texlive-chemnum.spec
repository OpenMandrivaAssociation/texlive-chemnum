Name:		texlive-chemnum
Version:	76924
Release:	1
Summary:	A method of numbering chemical compounds
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemnum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemnum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a \label- and \ref-like commands for
compound numbers. The package requires LaTeX 3 packages expl3
(from the l3kernel bundle) and xparse (from the l3packages
bundle).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemnum/chemnum.sty
%doc %{_texmfdistdir}/doc/latex/chemnum/README
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_en.tex
%doc %{_texmfdistdir}/doc/latex/chemnum/scheme-bla.ps
%doc %{_texmfdistdir}/doc/latex/chemnum/scheme-tmp.ps

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
