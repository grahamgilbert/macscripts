USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=set_desktops
PACKAGE_NAME=set_desktops
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
	set_desktop

set_desktop: l_Library_Management
	@sudo mkdir -p ${WORK_D}/Library/Management/set_desktops
	@sudo ${INSTALL} -m 755 -g wheel -o root set_desktops.py ${WORK_D}/Library/Management/set_desktops
