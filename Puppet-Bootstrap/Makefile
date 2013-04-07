USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=puppet_bootstrap
PACKAGE_NAME=puppet_bootstrap
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
    pack-script\
	pack-Library-LaunchDaemons-com.grahamgilbert.puppet_bootstrap.plist \
    
pack-script:
	@sudo mkdir -p ${WORK_D}/usr/local/puppet_bootstrap
	@sudo ${CP} puppet_bootstrap ${WORK_D}/usr/local/puppet_bootstrap/puppet_bootstrap
	@sudo chmod 700 ${WORK_D}/usr/local/puppet_bootstrap/puppet_bootstrap