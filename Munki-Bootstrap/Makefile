USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=Munki_Bootstrap
PACKAGE_NAME=Munki_Bootstrap
REVERSE_DOMAIN=com.pebbleit
PAYLOAD=\
	pack-file

pack-file: l_Users_Shared
	@sudo touch ${WORK_D}/Users/Shared/.com.googlecode.munki.checkandinstallatstartup
	@sudo chown root:wheel ${WORK_D}/Users/Shared/.com.googlecode.munki.checkandinstallatstartup