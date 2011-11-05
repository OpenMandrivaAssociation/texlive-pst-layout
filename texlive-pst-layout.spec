# revision 22586
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-layout
# catalog-date 2011-05-23 11:13:27 +0200
# catalog-license lppl
# catalog-version .95
Name:		texlive-pst-layout
Version:	.95
Release:	1
Summary:	Page layout macros based on PStricks packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-layout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-layout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-layout.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a means of creating elaborate ("pseudo-
tabular") layouts of material, typically to be overlaid on an
included graphic. The package requires a recent version of the
package pst-node and some other pstricks-related material.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/pst-layout/doc/latex/pst-layout/README
%doc %{_texmfdistdir}/doc/generic/pst-layout/doc/latex/pst-layout/pst-layout-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-layout/doc/latex/pst-layout/pst-layout-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-layout/tex/latex/pst-layout/pst-layout.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
