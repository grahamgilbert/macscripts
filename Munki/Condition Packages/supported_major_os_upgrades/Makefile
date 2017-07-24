USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=supported_major_os_upgrades
PACKAGE_NAME=supported_major_os_upgrades
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
    pack-script\
    
pack-script:
	@sudo mkdir -p ${WORK_D}/usr/local/munki/conditions
	@sudo ${INSTALL} -m 755 -g wheel -o root supported_major_os_upgrades ${WORK_D}/usr/local/munki/conditions/