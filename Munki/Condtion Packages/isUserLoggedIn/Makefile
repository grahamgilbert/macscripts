USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=isUserLoggedInCondition
PACKAGE_NAME=${TITLE}
REVERSE_DOMAIN=com.grahamgilbert
PACKAGE_VERSION=0.0.1
PAYLOAD=\
    pack-script\
    
pack-script:
	@sudo mkdir -p ${WORK_D}/usr/local/munki/conditions
	@sudo ${INSTALL} -m 755 -g wheel -o root isUserLoggedIn.sh ${WORK_D}/usr/local/munki/conditions/