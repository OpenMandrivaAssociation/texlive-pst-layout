# revision 25467
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-layout
# catalog-date 2011-05-27 12:35:46 +0200
# catalog-license lppl
# catalog-version .95
Name:		texlive-pst-layout
Version:	.95
Release:	3
Summary:	Page layout macros based on PStricks packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-layout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-layout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-layout.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means of creating elaborate ("pseudo-
tabular") layouts of material, typically to be overlaid on an
included graphic. The package requires a recent version of the
package pst-node and some other pstricks-related material.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-layout/pst-layout.sty
%doc %{_texmfdistdir}/doc/latex/pst-layout/README
%doc %{_texmfdistdir}/doc/latex/pst-layout/pst-layout-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pst-layout/pst-layout-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> .95-3
+ Revision: 779620
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> .95-2
+ Revision: 755320
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> .95-1
+ Revision: 719364
- texlive-pst-layout
- texlive-pst-layout
- texlive-pst-layout
- texlive-pst-layout

