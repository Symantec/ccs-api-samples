# Script to update any exising job details in the CCS system
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

# CCS Job URI
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Jobs"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Update the job details by providing the job name and Job GUID. we can get the job GUID by using search job by name API.
payload = "{\"JobDetails\":{\"JobDescription\": \"Update Job Description\",\"JobName\": \"Test_Job\"},\"JobID\":\"2a221e47-f38a-4a6b-af20-43d650e6d56b\"}"
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken,
    'Content-Type': "application/json"
    }
response = requests.request("PATCH", url, data=payload, headers=headers, verify=False)
print(response.text)
print(response.json)
