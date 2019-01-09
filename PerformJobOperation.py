# Script to perform the job operations. 'execute' and 'abort' operations are supported. Provide job GUID if you want to execute the job and provide job run ID if you want to abort the job. 
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

# Job Operation API endpoint URL. Provide Job GUID if you need to run the job.
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/jobs/0b3b6ac7-acc9-42f1-9db9-bf89d7bd6e16"
payload = "{\r\n\"Operation\":\"execute\"\r\n}\r\n"
# Provide Jobrun ID if you need to cancel/abort the job.
#url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/jobs/a348fb16-6d5b-4de3-bfd3-13f214a01538"
#payload = "{\r\n\"Operation\":\"abort\"\r\n}\r\n"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"   
    }
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
print(response.text)
print(response.json)
