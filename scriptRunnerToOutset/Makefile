USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=scriptRunnerToOutset
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD= \
	pack-script-postinstall \
	pack-usr-local-outset-on-demand-01-scriptRunnerToOutset_user_plist.py

l_usr_local_outset: l_usr_local
	@sudo mkdir -p ${WORK_D}/usr/local/outset/{boot-once,boot-every,login-once,login-every,on-demand,share,FoundationPlist}
	@sudo chown -R root:wheel ${WORK_D}/usr/local/outset
	@sudo chmod -R 755 ${WORK_D}/usr/local/outset

pack-usr-local-outset-login-once-%: % l_usr_local_outset
	@sudo ${INSTALL} -m 755 -g wheel -o root "${<}" ${WORK_D}/usr/local/outset/login-once
