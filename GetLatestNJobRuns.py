#Script to retrieve the list of latest runs for a specified job by providing job GUID in the request.
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

#Get Latest Job Runs API endpoint URL. Provide a job GUID to retrieve the job run details as per the job run count mentioned.
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Jobs/a282d163-2248-4904-8135-0eaf08be8e55/jobruns"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#Provide a count of the latest job runs that you want to retrieve.The default value of this parameter is 1.
querystring = {"count":"1"}

#Provide a count of the latest job runs that you want to retrieve.If you specify 0 in the Count field, the API returns all the job runs for the specified job GUID.
#querystring = {"count":"0"}

bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken
    }
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
print(response.text)
print(response.json)
