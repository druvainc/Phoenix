import requests
import time
import traceback
import json

# Import Libs required for Bearer Token OAuth2.0
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

# https://developer.druva.com/docs/get-bearer-token
client_id = ''
secret_key = ''

# 
api_url = "https://apis.druva.com/"

# https://developer.druva.com/reference#reference-getting-started
def get_token(client_id, secret_key):
	global auth_token
	auth = HTTPBasicAuth(client_id, secret_key)
	client = BackendApplicationClient(client_id=client_id)
	oauth = OAuth2Session(client=client)
	response = oauth.fetch_token(token_url='https://apis.druva.com/token', auth=auth)
	auth_token = response['access_token']
	expires_at = response['expires_at']


#
def get_api_call(auth_token, api_url, api_path):
    nextpage = None
    while True:
        # print nextpage
        nextpage = _get_api_call(auth_token, api_url, api_path, nextpage)
        if not nextpage:
            break
#
def _get_api_call(auth_token, api_url, api_path, nextpage):
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + auth_token}
    response = requests.get(api_url+api_path, headers=headers, params={'pageToken':nextpage})
    try:
        print 'Invoking API call'
        if response.status_code == 200:
            json_object = response.json()
            print json.dumps(json_object, indent=2)
            return response.json()['nextPageToken']
        elif response.status_code == 429:
            print 'Sleeping for 60 seconds'
            time.sleep(60)
            return _get_api_call(auth_token, api_url, api_path, nextpage)
        else:
            print 'Failure occured in API call.'
            print '[ERROR CODE] : ', response.status_code
    except Exception as e:
        print traceback.format_exc()

#
get_token(client_id, secret_key)
print 'Auth_token: ', auth_token

########################################################################
# Phoenix: API call to get Phoenix Audit trails across all Orgs.
print 'Phoenix Audit trails across all Orgs.'
api_path = "phoenix/audittrail/v1/orgs/" + str(0) + "/reports/list"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to get Storage usage.
print 'Phoenix Storage usage.'
api_path = "phoenix/storage/v1/orgs/" + str(0) + "/reports/usage"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to get Phoenix Alerts across all Orgs.
print 'Phoenix Alerts across all Orgs.'
api_path = "phoenix/alerts/v1/orgs/" + str(0) + "/alerts"
get_api_call(auth_token, api_url, api_path)
########################################################################


########################################################################
# FS

# Phoenix: API call to list all FS Backup Sets across all Orgs.
print 'FS Backup Sets across all Orgs.'
api_path = "phoenix/fileserver/v1/orgs/" + str(0) + "/reports/backupsets"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all FS Content Rules across all Orgs.
print 'FS Content Rules across all Orgs.'
api_path = "phoenix/fileserver/v1/orgs/" + str(0) + "/reports/contentrules"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all FS Jobs across all Orgs.
print 'FS Jobs across all Orgs.'
api_path = "phoenix/fileserver/v1/orgs/" + str(0) + "/reports/jobs"
get_api_call(auth_token, api_url, api_path)
########################################################################


########################################################################
# MSSQL

# Phoenix: API call to list all MSSQL Availability Groups across all Orgs.
print 'MSSQL Availability Groups across all Orgs.'
api_path = "phoenix/sqlserver/v1/orgs/" + str(0) + "/reports/availabilitygroup"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all MSSQL Backup Sets across all Orgs.
print 'MSSQL Backup Sets across all Orgs.'
api_path = "phoenix/sqlserver/v1/orgs/" + str(0) + "/reports/backupsets"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all MSSQL Instances across all Orgs.
print 'MSSQL Instances across all Orgs.'
api_path = "phoenix/sqlserver/v1/orgs/" + str(0) + "/reports/instances"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all MSSQL Jobs across all Orgs.
print 'MSSQL Jobs across all Orgs.'
api_path = "phoenix/sqlserver/v1/orgs/" + str(0) + "/reports/jobs"
get_api_call(auth_token, api_url, api_path)
########################################################################

########################################################################
# VMWare

# Phoenix: API call to list all VMWare Backup Sets across all Orgs.
print 'VMWare Backup Sets across all Orgs.'
api_path = "phoenix/vmware/v1/orgs/" + str(0) + "/reports/backupsets"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all VMWare backup proxies across all Orgs.
print 'VMWare backup proxies across all Orgs.'
api_path = "phoenix/vmware/v1/orgs/" + str(0) + "/reports/proxies"
get_api_call(auth_token, api_url, api_path)

# Phoenix: API call to list all VMWare Jobs across all Orgs.
print 'VMWare Jobs across all Orgs.'
api_path = "phoenix/vmware/v1/orgs/" + str(0) + "/reports/jobs"
get_api_call(auth_token, api_url, api_path)
########################################################################

########################################################################
# Phoenix: API call to list all Backup Failure Alerts across all Orgs.
print 'Backup Failure Alerts across all Orgs.'
api_path = "phoenix/alerts/v1/orgs/" + str(0) + "/alerts/jobs/backupFailures"
get_api_call(auth_token, api_url, api_path)
########################################################################