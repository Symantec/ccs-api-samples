#Script to get evaluation result in raw JSON format for a specified standard and a specified asset in CCS. 
#For more Details, Refer to CCS REST API document at: https://apidocs.symantec.com/home/CCS

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Declare Variables 
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
	return token

#Get Evaluation Result API endpoint URL.
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Results"

#Provide assetid, standardid and jobrunid to get the evaluation result of specific asset, standard and job run.
payload = "{\"assetid\" : \"7ca3a38e-1e51-42ef-8b5d-88813eae0c14\", \"standardid\" : \"6b020d29-5fe8-47d0-bd89-ccd3339a5ebe\", \"jobrunid\" : \"cae05ae3-8454-43a9-9139-f678b66decf7\"}"


#If you want to get the evaluation result of specific standard version, Please speificy standard version parameter. In this case, jobrunid parameter is not needed.
#payload = "{\"assetid\" : \"7ca3a38e-1e51-42ef-8b5d-88813eae0c14\", \"standardid\" : \"6b020d29-5fe8-47d0-bd89-ccd3339a5ebe\", \"standardversion\" : \"1.3.0\"}"

#To fetch the latest evaluation result of specific standard and asset, just mention asset id and standard id. 
#payload = "{\"assetid\" : \"7ca3a38e-1e51-42ef-8b5d-88813eae0c14\", \"standardid\" : \"6b020d29-5fe8-47d0-bd89-ccd3339a5ebe\"}"

#To fetch the raw result for specific checks in the standard, you need to provide a list of check IDs in the checkidlist parameter.
#payload = "{\"assetid\" : \"df8ce907-7c21-46d7-9372-79a5f5736088\", \"standardid\" : \"f61462b9-8f18-4e39-9e81-509e530fc231\", \"checkidlist\" : [\"7673bba8-1933-41ce-98d8-7fa7cca60c9f\",\"f8e64a6c-abe5-4eab-bfe9-19f1c4ad0c85\",\"62a3ce34-c54b-4800-9c87-2a31bcd7de66\",\"0f2a0ae1-150c-4658-b9c0-bfb6e17693c7\"]}"


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
print("\n Bearer Token is:\n")
print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"   
    }
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
print(response.text)
print(response.json)
