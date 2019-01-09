# Script to Delete the Standard from CCS system
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
# CCS Standard URI
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Standards"
# Provide the standard details which need to be deleted. we can provide standard name or standard GUID
payload = "{\"StandardList\":[{\"Type\":\"Name\",\"Standards\":[\"Test Standard for AIX\",\"Test Windows 2012\"]},{\"Type\":\"ID\",\"Standards\":[\"77fd3e2e4e7e1800-3775-4ba8-9b9d-37d16cccd5a7\",\"3a9abc89-ae28-46ec-ab6f-0885e40e90e1\",\"78d3c003-5f02-4d39-82b8-a90a8613167c\"]}],\"ContainerPath\":\"standards\",\"DeletePredefinedStandard\":\"false\"}"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }
response = requests.request("DELETE", url, data=payload, headers=headers, verify=False)
print(response.text)
print(response.json)
