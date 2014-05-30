USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make

TITLE=ClearReg
PACKAGE_NAME=ClearReg
REVERSE_DOMAIN=com.grahamgilbert
PAYLOAD=\
	pack-AppleSetupDone \
	pack-SetupRegComplete
    
pack-AppleSetupDone:
	@sudo mkdir -p ${WORK_D}/var/db/
	@sudo touch ${WORK_D}/var/db/.AppleSetupDone
	@sudo chown root:wheel ${WORK_D}/var/db/.AppleSetupDone

pack-SetupRegComplete:
	@sudo mkdir -p ${WORK_D}/Library/Receipts/
	@sudo touch ${WORK_D}/Library/Receipts/.SetupRegComplete
	@sudo chown root:wheel ${WORK_D}/Library/Receipts/.SetupRegComplete