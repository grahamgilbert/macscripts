USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=Composer
PACKAGE_NAME=${TITLE}
REVERSE_DOMAIN=com.jamf
PAYLOAD=\
	pack-app

pack-app: l_Applications
	@sudo ${DITTO} "/Applications/Composer.app" ${WORK_D}/Applications/Composer.app
	@sudo chown -R root:wheel ${WORK_D}/Applications/Composer.app
	@sudo chmod -R 755 ${WORK_D}/Applications/Composer.app