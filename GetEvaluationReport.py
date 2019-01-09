# Script to Generate evaluation report in excel format
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

# CCS Report URI
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Reports"
# Provide the Asset GUID, Standard GUID, Job GUID and Report file type as "excel".  
querystring = {"assetid":"<AssetID>", "standardid":"<StandardID>", "reportfiletype":"excel", "jobrunid":"<JobRunID>"}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
print(response.text)
print(response.json)
