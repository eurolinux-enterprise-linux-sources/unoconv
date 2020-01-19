Summary:   Tool to convert between any document format supported by LibreOffice
Name:      unoconv
Version:   0.6
Release:   5%{?dist}
License:   GPLv2
Group:     System Environment/Base
URL:       http://dag.wieers.com/home-made/unoconv/
Source:    http://dag.wieers.com/home-made/%{name}/%{name}-%{version}.tar.gz
Patch0:    0001-Fix-a-broken-export-option-and-add-V-as-alternative-.patch
Patch1:    0001-python3-added-compatibility.patch
Patch2:    0001-update-FSF-address.patch

BuildArch: noarch
Requires:  libreoffice-core
Requires:  libreoffice-pyuno

%description
unoconv converts between any document format that LibreOffice understands.
It uses LibreOffice's UNO bindings for non-interactive conversion of
documents.

Supported document formats include Open Document Format (.odf), MS Word (.doc),
MS Office Open/MS OOXML (.xml), Portable Document Format (.pdf), HTML, XHTML,
RTF, Docbook (.xml), and more.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%install
make install DESTDIR="%{buildroot}"
pushd %{buildroot}/%{_bindir}
%if 0%{?fedora} >= 19
    mv %{name}3.py %{name}
    rm %{name}2.py
%else
    mv %{name}2.py %{name}
    rm %{name}3.py
%endif
popd


%files
%doc AUTHORS ChangeLog COPYING README.asciidoc WISHLIST doc/*.txt tests/
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Tue Jul 23 2013 David Tardon <dtardon@redhat.com> - 0.6-5
- Resolves: rhbz#987046 drop env from shebang

* Wed May 29 2013 David Tardon <dtardon@redhat.com> - 0.6-4
- rhbz#957776 cannot open office documents

* Mon Apr 08 2013 David Tardon <dtardon@redhat.com> - 0.6-3
- Resolves: rhbz#947096 unoconv doesn't work with Libreoffice 4.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 David Tardon <dtardon@redhat.com> - 0.6-1
- new upstream release

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 David Tardon <dtardon@redhat.com> - 0.5-1
- new upstream release

* Mon Mar 26 2012 David Tardon <dtardon@redhat.com> - 0.4-6

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-3
- Add missing Requires on openoffice.org-brand/libreoffice-core. RHBZ#658576

* Sat Nov 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-2
- Backport some upstream fixes (LD_LIBRARY_PATH issue and -o flag issue)

* Fri Nov 12 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.4-1
- Update to 0.4

* Sat Oct 30 2010 Caolán McNamara <caolanm@redhat.com> - 0.3-5
- rebuild for LibreOffice

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.3-3
- Fix rpmlints
- Prepare package for Fedora review

* Sun Feb 22 2009 Peter Hanecak <hany@hany.sk> 0.3-2
- used %%{?dist} in release number
- license GPLv2

* Wed Dec 19 2007 Dag Wieers <dag@wieers.com> - 0.3-2 - 5993+/dag
- Fixed openoffice.org2 dependency on RHEL4.

* Sat Sep 01 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Sun May 20 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Sat May 19 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
