USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=shard_munki_condition
PACKAGE_NAME=${TITLE}
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
    pack-script\

pack-script:
	@sudo mkdir -p ${WORK_D}/usr/local/munki/conditions
	@sudo ${INSTALL} -m 755 -g wheel -o root shard ${WORK_D}/usr/local/munki/conditions/
