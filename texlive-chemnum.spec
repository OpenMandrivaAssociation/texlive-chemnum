# revision 24809
# category Package
# catalog-ctan /macros/latex/contrib/chemnum
# catalog-date 2011-12-09 11:13:13 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-chemnum
Version:	0.4
Release:	2
Summary:	A method of numbering chemical compounds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemnum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemnum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemnum.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a \label- and \ref-like commands for
compound numbers. The package requires LaTeX 3 packages expl3
(from the l3experimental bundle) and xparse (from the
l3packages bundle).

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
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum-codehelper.tex
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_doc_de.pdf
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_doc_de.tex
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_doc_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemnum/chemnum_doc_en.tex
%doc %{_texmfdistdir}/doc/latex/chemnum/scheme-bla.eps
%doc %{_texmfdistdir}/doc/latex/chemnum/scheme-tmp.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
