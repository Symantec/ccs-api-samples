#Script to retrieve the list of standards based on the search criteria mentioned in the request.
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

#Search Standard API endpoint URL
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/Standards"

#Search based on displayName of the standard and by using Contains Operator
querystring = {"attributes":"displayName Contains red hat", "ContainerPath":"standards\\predefined\\unix", "Searchsubtree":"true"}

#Search based on Symc-Standard-Author of the standard by using '=' Operator and displayName of the standard by using StartsWith Operator
#querystring = {"attributes":"displayName Contains cis,Symc-Standard-Author=symantec", "ContainerPath":"standards\\predefined\\unix", "Searchsubtree":"true"}

#Search based on displayName of the standard and TargetTypeIDs
#querystring = {"attributes":"displayName Contains apache,symc-Standard-TargetTypeIDs=97546792-56b0-4020-9d88-f8786371f2d9", "ContainerPath":"standards\\predefined\\unix", "Searchsubtree":"true"}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"   
    }
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
print(response.text)
print(response.json)
