import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

urlToken = "https://<hostname>:<port number>/ccs/api/v1/oauth/tokens"

payload = "grant_type=password&username=<user name>&password=<password>"
headers = {
   	'Content-Type': "application/json",
}
responseToken = requests.request("POST", urlToken, data=payload, headers=headers, verify=False)

tokenDict = responseToken.json()
token = tokenDict['access_token']
refreshToken = tokenDict['refresh_token']

print(responseToken.text)
print(responseToken.json)
