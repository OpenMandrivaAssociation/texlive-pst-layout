Name:		texlive-pst-layout
Version:	.95
Release:	2
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
%{_texmfdistdir}/tex/latex/pst-layout
%doc %{_texmfdistdir}/doc/latex/pst-layout

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
