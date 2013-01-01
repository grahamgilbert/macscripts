include /usr/local/share/luggage/luggage.make

TITLE=login_item
PACKAGE_NAME=login_item
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
	pack-script-postflight\
    pack-file\
    
pack-file:
    @sudo mkdir -p ${WORK_D}/tmp
	@sudo mkdir -p ${WORK_D}/usr/local/management
	@sudo ${CP} theLoginItem ${WORK_D}/usr/local/management/theLoginItem
	@sudo ${CP} com.grahamgilbert.loginitem.plist ${WORK_D}/tmp/com.grahamgilbert.loginitem.plist