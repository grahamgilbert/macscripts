#!/bin/sh

# This was stolen from DeployStudio. I didn't write it, but dammit, I'm going to use it.

#
# Script config
#

AD_DOMAIN="ad.company.com"
COMPUTER_ID=`/usr/sbin/scutil --get LocalHostName`
COMPUTERS_OU="OU=Macs,OU=London,DC=ad,DC=company,DC=com"
ADMIN_LOGIN="bindUser"
ADMIN_PWD="bindPassword"
MOBILE="enable"
MOBILE_CONFIRM="disable"
LOCAL_HOME="enable"
USE_UNC_PATHS="enable"
UNC_PATHS_PROTOCOL="smb"
PACKET_SIGN="allow"
PACKET_ENCRYPT="allow"
PASSWORD_INTERVAL="0"
ADMIN_GROUPS="COMPANY\Domain Admins,COMPANY\Enterprise Admins"

# UID_MAPPING=
# GID_MAPPING=
# GGID_MAPPING==

# disable history characters
histchars=

SCRIPT_NAME=`basename "${0}"`

echo "${SCRIPT_NAME} - v1.26 ("`date`")"

#
# functions
#
is_ip_address() {
  IP_REGEX="\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
  IP_CHECK=`echo ${1} | egrep ${IP_REGEX}`
  if [ ${#IP_CHECK} -gt 0 ]
  then
    return 0
  else
    return 1
  fi
}


#
# Wait for the naming script to have run
#
if [ ${COMPUTER_ID} -eq "" ]
then
echo "The mac doesn't have a name, exiting."
  exit 1
fi

# AD can only use a 15 character name
COMPUTER_ID=`echo ${COMPUTER_ID} | cut -c1-15`

#
# Wait for network services to be initialized
#
echo "Checking for the default route to be active..."
ATTEMPTS=0
MAX_ATTEMPTS=18
while ! (netstat -rn -f inet | grep -q default)
do
  if [ ${ATTEMPTS} -le ${MAX_ATTEMPTS} ]
  then
    echo "Waiting for the default route to be active..."
    sleep 10
    ATTEMPTS=`expr ${ATTEMPTS} + 1`
  else
    echo "Network not configured, AD binding failed (${MAX_ATTEMPTS} attempts), will retry at next boot!" 2>&1
    exit 1
  fi
done

#
# Wait for the related server to be reachable
# NB: AD service entries must be correctly set in DNS
#
SUCCESS=
is_ip_address "${AD_DOMAIN}"
if [ ${?} -eq 0 ]
then
  # the AD_DOMAIN variable contains an IP address, let's try to ping the server
  echo "Testing ${AD_DOMAIN} reachability" 2>&1  
  if ping -t 5 -c 1 "${AD_DOMAIN}" | grep "round-trip"
  then
    echo "Ping successful!" 2>&1
    SUCCESS="YES"
  else
    echo "Ping failed..." 2>&1
  fi
else
  ATTEMPTS=0
  MAX_ATTEMPTS=12
  while [ -z "${SUCCESS}" ]
  do
    if [ ${ATTEMPTS} -lt ${MAX_ATTEMPTS} ]
    then
      AD_DOMAIN_IPS=( `host "${AD_DOMAIN}" | grep " has address " | cut -f 4 -d " "` )
      for AD_DOMAIN_IP in ${AD_DOMAIN_IPS[@]}
      do
        echo "Testing ${AD_DOMAIN} reachability on address ${AD_DOMAIN_IP}" 2>&1  
        if ping -t 5 -c 1 ${AD_DOMAIN_IP} | grep "round-trip"
        then
          echo "Ping successful!" 2>&1
          SUCCESS="YES"
        else
          echo "Ping failed..." 2>&1
        fi
        if [ "${SUCCESS}" = "YES" ]
        then
          break
        fi
      done
      if [ -z "${SUCCESS}" ]
      then
        echo "An error occurred while trying to get ${AD_DOMAIN} IP addresses, new attempt in 10 seconds..." 2>&1
        sleep 10
        ATTEMPTS=`expr ${ATTEMPTS} + 1`
      fi
    else
      echo "Cannot get any IP address for ${AD_DOMAIN} (${MAX_ATTEMPTS} attempts), aborting lookup..." 2>&1
      break
    fi
  done
fi

if [ -z "${SUCCESS}" ]
then
  echo "Cannot reach any IP address of the domain ${AD_DOMAIN}." 2>&1
  echo "AD binding failed, will retry at next boot!" 2>&1
  exit 1
fi

#
# Unbinding computer first
#
echo "Unbinding computer..." 2>&1
dsconfigad -remove -username "${ADMIN_LOGIN}" -password "${ADMIN_PWD}" 2>&1

#
# Try to bind the computer
#
ATTEMPTS=0
MAX_ATTEMPTS=12
SUCCESS=
while [ -z "${SUCCESS}" ]
do
  if [ ${ATTEMPTS} -le ${MAX_ATTEMPTS} ]
  then
    echo "Binding computer to domain ${AD_DOMAIN}..." 2>&1 
    dsconfigad -add "${AD_DOMAIN}" -computer "${COMPUTER_ID}" -ou "${COMPUTERS_OU}" -username "${ADMIN_LOGIN}" -password "${ADMIN_PWD}" -force 2>&1
    IS_BOUND=`dsconfigad -show | grep "Active Directory Domain"`
    if [ -n "${IS_BOUND}" ]
    then
      SUCCESS="YES"
    else
      echo "An error occured while trying to bind this computer to AD, new attempt in 10 seconds..." 2>&1
      sleep 10
      ATTEMPTS=`expr ${ATTEMPTS} + 1`
    fi
  else
    echo "AD binding failed (${MAX_ATTEMPTS} attempts), will retry at next boot!" 2>&1
    SUCCESS="NO"
  fi
done

if [ "${SUCCESS}" = "YES" ]
then
  #
  # Update AD plugin options
  #
  echo "Setting AD plugin options..." 2>&1
  dsconfigad -mobile ${MOBILE} 2>&1
  sleep 1
  dsconfigad -mobileconfirm ${MOBILE_CONFIRM} 2>&1 
  sleep 1
  dsconfigad -localhome ${LOCAL_HOME} 2>&1
  sleep 1
  dsconfigad -useuncpath ${USE_UNC_PATHS} 2>&1
  sleep 1
  dsconfigad -protocol ${UNC_PATHS_PROTOCOL} 2>&1
  sleep 1
  dsconfigad -packetsign ${PACKET_SIGN} 2>&1
  sleep 1
  dsconfigad -packetencrypt ${PACKET_ENCRYPT} 2>&1
  sleep 1
  dsconfigad -passinterval ${PASSWORD_INTERVAL} 2>&1
  if [ -n "${ADMIN_GROUPS}" ]
  then
    sleep 1
    dsconfigad -groups "${ADMIN_GROUPS}" 2>&1
  fi
  sleep 1

  if [ -n "${AUTH_DOMAIN}" ] && [ "${AUTH_DOMAIN}" != 'All Domains' ]
  then
    dsconfigad -alldomains disable 2>&1
  else
    dsconfigad -alldomains enable 2>&1
  fi
  AD_SEARCH_PATH=`dscl /Search -read / CSPSearchPath | grep "Active Directory" | sed 's/^ *//' | sed 's/ *$//'`
  if [ -n "${AD_SEARCH_PATH}" ]
  then
    echo "Deleting '${AD_SEARCH_PATH}' from authentication search path..." 2>&1
    dscl localhost -delete /Search CSPSearchPath "${AD_SEARCH_PATH}" 2>/dev/null
    echo "Deleting '${AD_SEARCH_PATH}' from contacts search path..." 2>&1
    dscl localhost -delete /Contact CSPSearchPath "${AD_SEARCH_PATH}" 2>/dev/null
  fi
  dscl localhost -create /Search SearchPolicy CSPSearchPath 2>&1
  dscl localhost -create /Contact SearchPolicy CSPSearchPath 2>&1
  AD_DOMAIN_NODE=`dscl localhost -list "/Active Directory" | head -n 1`
  if [ "${AD_DOMAIN_NODE}" = "All Domains" ]
  then
    AD_SEARCH_PATH="/Active Directory/All Domains"
  elif [ -n "${AUTH_DOMAIN}" ] && [ "${AUTH_DOMAIN}" != 'All Domains' ]
  then
    AD_SEARCH_PATH="/Active Directory/${AD_DOMAIN_NODE}/${AUTH_DOMAIN}"
  else
    AD_SEARCH_PATH="/Active Directory/${AD_DOMAIN_NODE}/All Domains"
  fi
  echo "Adding '${AD_SEARCH_PATH}' to authentication search path..." 2>&1
  dscl localhost -append /Search CSPSearchPath "${AD_SEARCH_PATH}"
  echo "Adding '${AD_SEARCH_PATH}' to contacts search path..." 2>&1
  dscl localhost -append /Contact CSPSearchPath "${AD_SEARCH_PATH}"

  if [ -n "${UID_MAPPING}" ]
  then
    sleep 1
    dsconfigad -uid "${UID_MAPPING}" 2>&1
  fi
  if [ -n "${GID_MAPPING}" ]
  then
    sleep 1
    dsconfigad -gid "${GID_MAPPING}" 2>&1
  fi
  if [ -n "${GGID_MAPPING}" ]
  then
    sleep 1
    dsconfigad -ggid "${GGID_MAPPING}" 2>&1
  fi

  GROUP_MEMBERS=`dscl /Local/Default -read /Groups/com.apple.access_loginwindow GroupMembers 2>/dev/null`
  NESTED_GROUPS=`dscl /Local/Default -read /Groups/com.apple.access_loginwindow NestedGroups 2>/dev/null`
  if [ -z "${GROUP_MEMBERS}" ] && [ -z "${NESTED_GROUPS}" ]
  then
    echo "Enabling network users login..." 2>&1
    dseditgroup -o edit -n /Local/Default -a netaccounts -t group com.apple.access_loginwindow 2>/dev/null
  fi

  #
  # Self-removal 
  #
  if [ "${SUCCESS}" = "YES" ]
  then
    if [ -e "/System/Library/CoreServices/ServerVersion.plist" ]
    then
      DEFAULT_REALM=`more /Library/Preferences/edu.mit.Kerberos | grep default_realm | awk '{ print $3 }'`
      if [ -n "${DEFAULT_REALM}" ]
      then
        echo "The binding process looks good, will try to configure Kerberized services on this machine for the default realm ${DEFAULT_REALM}..." 2>&1
        /usr/sbin/sso_util configure -r "${DEFAULT_REALM}" -a "${ADMIN_LOGIN}" -p "${ADMIN_PWD}" all
      fi
      #
      # Give OD a chance to fully apply new settings
      #
      echo "Applying changes..." 2>&1
      sleep 10
    fi
    if [ -e "${CONFIG_FILE}" ]
    then
      /usr/bin/srm -mf "${CONFIG_FILE}"
    fi
    /usr/bin/srm -mf "${0}"
    exit 0
  fi
fi

exit 1