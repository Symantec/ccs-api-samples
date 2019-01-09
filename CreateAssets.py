# Script to create asset or add asset in the CCS system 
# For more details Refer the CCS REST API document at : https://apidocs.symantec.com/home/CCS

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Variable 
# Replace the <hostname> with CCS application server host name
# Replace the <port number> with the configured port number for REST API, Default Port Number : 12431
# Replace the <user name> and <password> with valid CCS user name and password for example: UserName = domain1\\administrator, password = pass@123   
HostName = '<hostname>'
PortNumber = '<port number>'
UserName = '<user name>'
Password = '<password>'

# Function to generate CCS REST API access token
def getToken():
	urlToken = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&username=" + UserName + "&password=" + Password +""
	headers = {'Content-Type': "application/json"}
	responseToken = requests.request("POST", urlToken, data=payload, headers=headers, verify=False)
	autheticationresult = responseToken.status_code
	if (autheticationresult!=200) :
		print("\nToken Generation Failed. Please check if the REST API is enabled and User name and password is correct\n")
		exit()
	tokenDict = responseToken.json()
	token = tokenDict['access_token']
	refreshToken = tokenDict['refresh_token']
	print("bearer Token is:\n")
	print(token)
	print("\n Refresh Token is:\n")
	print(refreshToken)
	return token
# CCS REST Assets URI
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/assets"
# Payload for adding single windows asset 
payload = "[{ \"Type\" : \"symc-csm-AssetSystem-Asset-Wnt-Machine\",\"symc-csm-AssetSystem-Asset-Wnt-Machine-HostName\" : \"MyWinAsset\",\"symc-csm-AssetSystem-Asset-Wnt-Machine-DomainWorkgroupName\" : \"NewDomain\" }]"
# Payload for adding multiple assets 
#payload = "[{\"Type\" : \"symc-csm-AssetSystem-Asset-Wnt-Machine\",\"symc-csm-AssetSystem-Asset-Wnt-Machine-HostName\" : \"MytestWinAsset7\",\"symc-csm-AssetSystem-Asset-Wnt-Machine-DomainWorkgroupName\" : \"MyDomain\"},{\"Type\" : \"symc-csm-AssetSystem-Asset-Cisco-Router\",\"symc-csm-AssetSystem-Asset-Cisco-Router-IPAddress\" : \"10.211.886.888\"},{\"Type\" : \"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-HOSTMACHINE\" : \"testredhatx86123\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-IPAddress\" : \"10.211.88.111\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-InstancePortNumber\" : \"5704\"},{\"Type\" : \"symc-csm-AssetSystem-Asset-Unix-Machine\",\"symc-csm-AssetSystem-Asset-Unix-Machine-IPAddress\" : \"10.211.66.119\" ,\"symc-csm-AssetSystem-Asset-Unix-Machine-HostMachine\" : \"rhelx86789\"},{\"Type\" : \"symc-csm-AssetSystem-Asset-Dbif-server\",\"symc-csm-AssetSystem-Asset-Dbif-server-SQLServerDomainName\" : \"MyDomain\",\"symc-csm-AssetSystem-Asset-Dbif-server-hostName\" : \"MySQLHost1\",\"symc-csm-AssetSystem-Asset-Dbif-server-serverName\" : \"SQLServerAsset\"},{\"Type\" : \"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers\",\"container\" : \"Assets\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-HOSTMACHINE\" : \"AKwin2012r2\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-IPAddress\" : \"10.211.98.98\",\"symc-csm-AssetSystem-Asset-Unix-MySQL-Servers-InstancePortNumber\" : \"5701\"}]"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
print(response.text)
print(responce.json)
