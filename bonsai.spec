%define name		bonsai
%define version		1.3.9
%define snapshot	20051228
%define release		%mkrel 0.%{snapshot}.7

%define _requires_exceptions perl(\\(CGI.pl\\|SourceChecker\\))

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A query interface to the CVS source repository
License:	MPL
Group:		Networking/WWW
URL:		http://www.mozilla.org/projects/bonsai/
Source0:	%{name}-%{snapshot}.tar.bz2
Source1:	%{name}.README.mdk.bz2
Patch0:		%{name}-20051228.fhs.patch
Requires:	perl-DBD-mysql
%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Bonsai is a really cool idea on how to "see" changes taking place during a
development cycle. The original implementation was by Terry Weissman, first
done in TCL, then later ported to Perl. It's built to run against CVS using
Perl, MySQL, and your favorite webserver to display checkin history, log
information, diffs, and other assorted pieces of information in easy to parse
HTML.

%prep
%setup -q -n %{name}
%patch0 -p1

find . -name CVS -o -name .cvsignore | xargs rm -rf

# fix paths
find . -type f | xargs perl -pi -e "s|/usr/bonsaitools/bin|%{_bindir}|g"

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_var}/www/%{name}
install -m 755 *.cgi %{buildroot}%{_var}/www/%{name}
cp -pr *.html *.gif robots.txt %{buildroot}%{_var}/www/%{name}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/lib
install -d -m 755 %{buildroot}%{_datadir}/%{name}/bin
install -m 644 CGI.pl \
		addcheckin.pl \
		adminfuncs.pl \
		adminmail.pl \
		createlegaldirs.pl \
		cvsblame.pl \
		cvsindex.pl \
		cvsmenu.pl \
		cvsquery.pl \
		defparams.pl \
		dolog.pl \
		get_line.pl \
		globals.pl \
		handleAdminMail.pl \
		handleCheckinMail.pl \
		header.pl \
		indextest.pl \
		lloydcgi.pl \
		modules.pl \
		processqueue.pl \
		reposfiles.pl \
		testlock.pl \
		%{buildroot}%{_datadir}/%{name}/lib
install -m 755 addcheckin.pl \
		adminmail.pl \
		createlegaldirs.pl \
		cvsblame.pl \
		cvsindex.pl \
		handleAdminMail.pl \
		handleCheckinMail.pl \
		processqueue.pl \
		reposfiles.pl \
		testlock.pl \
		maketables.sh \
		trapdoor \
		%{buildroot}%{_datadir}/%{name}/bin

install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}

install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 treeconfig.pl.in %{buildroot}%{_sysconfdir}/%{name}/treeconfig.pl
install -m 644 cvsgraph.conf %{buildroot}%{_sysconfdir}/%{name}

# apache configuration
install -d -m 755 %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{name}.conf <<EOF
# %{name} Apache configuration
Alias /%{name} %{_var}/www/%{name}

<Directory %{_var}/www/%{name}>
    Options ExecCGI
    DirectoryIndex toplevel.cgi
    Allow from all
</Directory>
EOF

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201010
%_post_webapp
%endif

%postun
%if %mdkversion < 201010
%_postun_webapp
%endif

%files
%defattr(-,root,root)
%doc README INSTALL CHANGES
%config(noreplace) %{_webappconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}
%{_var}/www/%{name}
%{_datadir}/%{name}
%attr(-,apache,apache) %{_localstatedir}/lib/%{name}
