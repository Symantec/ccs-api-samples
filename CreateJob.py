#Script to create a job of type 'Collection Evaluation', 'Data Collection' and 'Evaluation'. 
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

#Create Job API endpoint URL.
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/jobs"

#Provide Asset GUID and Asset Type, ,Standard GUID, job name and Job type.Supported Job Types for job creation: CollectionEvaluationJob, CollectionJob, EvaluationJob.
#Asset GUID and Asset Type can be retrieved by using SearchAsset API, Standard GUID can be retrieved by using Search Standard API.
#Following is the example of creating CollectionEvaluation job with minimal required parameters. It will only create the job.
payload = "{\"JobDetails\":{\"AssetsResolutionInfo\": [{\"Id\": \"d387d8b5-6278-4bcb-83c7-b55d2072d2a8\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"}],\"JobDescription\": \"Test CER Job\",\"JobName\": \"Test_Job11\",\"Standards\": [\"6b020d29-5fe8-47d0-bd89-ccd3339a5ebe\"]},\"JobType\":\"CollectionEvaluationJob\"}"

#Following is the example of creating job with runnow parameter set to true. It will create the job and run the job.
#In this example, 'runnow' parameter is set to true.
#payload = "{\"JobDetails\":{\"AssetsResolutionInfo\": [{\"Id\": \"d387d8b5-6278-4bcb-83c7-b55d2072d2a8\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"}],\"JobDescription\": \"Demo Data Collection Job\",\"JobName\": \"A1_CollectionJob_RUNOW\",\"Standards\": [\"6B020D29-5FE8-47D0-BD89-CCD3339A5EBE\"],\"Schedule\": {\"EndJobRunConfigured\": false, \"EndJobRunTimeInterval\": \"00:00:00\",\"SubScheduleRepeatDays\": 0,\"SubScheduleRepeatPeriodDays\": 0,\"MonthlyDay\": 0,\"MonthlyDayOfTheWeek\": 0,\"MonthlyIsByOrdinalDay\": false,\"MonthlyOrdinalDay\": 0, \"MonthlyRecurEvery\": 0, \"RecurrenceType\": 0,\"RepeatDays\": 50,\"RepeatMinutes\": 0,\"RunEveryNDays\": true,\"RunNow\": true,\"RunOnce\": false,\"RunPeriodically\": false,\"StartDate\": \"2018-11-18T02:14:27.5120788-08:00\", \"WeeklyDay\": 0, \"WeeklyRecurEvery\": 0}},\"JobType\":\"CollectionJob\"}"

#Following is the example of creating job and shcedule a job run. It will create the job and schedule the job run as mentioned in the input URL.
#In this example, RunPeriodically parameter is set to true.
#payload = "{\"JobDetails\":{\"AssetsResolutionInfo\": [{\"Id\": \"d387d8b5-6278-4bcb-83c7-b55d2072d2a8\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"}],\"JobDescription\": \"Demo Data Collection Job by scheduling it\",\"JobName\": \"A1_CollectionJob_ScheduleRun\",\"Standards\": [\"6B020D29-5FE8-47D0-BD89-CCD3339A5EBE\"],\"Schedule\": {\"EndJobRunConfigured\": false, \"EndJobRunTimeInterval\": \"00:00:00\",\"SubScheduleRepeatDays\": 0,\"SubScheduleRepeatPeriodDays\": 0,\"MonthlyDay\": 0,\"MonthlyDayOfTheWeek\": 0,\"MonthlyIsByOrdinalDay\": false,\"MonthlyOrdinalDay\": 0, \"MonthlyRecurEvery\": 0, \"RecurrenceType\": 0,\"RepeatDays\": 50,\"RepeatMinutes\": 0,\"RunEveryNDays\": true,\"RunNow\": false,\"RunOnce\": false,\"RunPeriodically\": true,\"StartDate\": \"2019-01-05T04:10:27.5120788-08:00\", \"WeeklyDay\": 0, \"WeeklyRecurEvery\": 0}},\"JobType\":\"CollectionJob\"}"

#Following is the example of creating job with multiple assets.
#In this example, multiple asset IDs are mentioned under AssetsResolutionInfo.
#payload = "{\"JobDetails\":{\"AssetsResolutionInfo\": [{\"Id\": \"d387d8b5-6278-4bcb-83c7-b55d2072d2a8\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"},{\"Id\": \"1169462b-e9bd-46f4-827a-7ac9b1a220d1\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"}],\"JobDescription\": \"Demo Data Collection Job on muktiple assets\",\"JobName\": \"A1_CollectionJob_MultipleAssets\",\"Standards\": [\"6B020D29-5FE8-47D0-BD89-CCD3339A5EBE\"],\"Schedule\": {\"EndJobRunConfigured\": false, \"EndJobRunTimeInterval\": \"00:00:00\",\"SubScheduleRepeatDays\": 0,\"SubScheduleRepeatPeriodDays\": 0,\"MonthlyDay\": 0,\"MonthlyDayOfTheWeek\": 0,\"MonthlyIsByOrdinalDay\": false,\"MonthlyOrdinalDay\": 0, \"MonthlyRecurEvery\": 0, \"RecurrenceType\": 0,\"RepeatDays\": 50,\"RepeatMinutes\": 0,\"RunEveryNDays\": true,\"RunNow\": true,\"RunOnce\": false,\"RunPeriodically\": false,\"StartDate\": \"2018-11-18T02:14:27.5120788-08:00\", \"WeeklyDay\": 0, \"WeeklyRecurEvery\": 0}},\"JobType\":\"CollectionJob\"}"

#Following is the example of creating and running job with success and failure notifications.
#In this example, You need to configure your FailureNotification and SuccessNotification.
#payload = "{\"JobDetails\":{\"AssetsResolutionInfo\": [{\"Id\": \"d387d8b5-6278-4bcb-83c7-b55d2072d2a8\",\"Type\": \"symc-csm-AssetSystem-Asset-Unix-Machine\"}],\"JobDescription\": \"Demo Data Collection Job with notifications\",\"JobName\": \"A1_CollectionJob_RUNOW_WithNotifications\",\"Standards\": [\"6B020D29-5FE8-47D0-BD89-CCD3339A5EBE\"],\"FailureNotification\":{\"FromEmailAddress\":\"arti@ccsqa.local\",\"Subject\":\"Collection-Evaluation-Reporting job failed\",\"ToEmailAddress\":\"chetan@ccsqa.local\",\"Body\":\"Failure notification message\"},\"SuccessNotification\":{\"FromEmailAddress\":\"arti@ccsqa.local\",\"Subject\":\"Collection-Evaluation-Reporting job completed successfully\",\"ToEmailAddress\":\"chetan@ccsqa.local\",\"Body\":\"Success notification message\"},\"ShouldSendFailureNotification\":\"true\",\"ShouldSendSuccessNotification\":\"true\",\"Schedule\": {\"EndJobRunConfigured\": false, \"EndJobRunTimeInterval\": \"00:00:00\",\"SubScheduleRepeatDays\": 0,\"SubScheduleRepeatPeriodDays\": 0,\"MonthlyDay\": 0,\"MonthlyDayOfTheWeek\": 0,\"MonthlyIsByOrdinalDay\": false,\"MonthlyOrdinalDay\": 0, \"MonthlyRecurEvery\": 0, \"RecurrenceType\": 0,\"RepeatDays\": 50,\"RepeatMinutes\": 0,\"RunEveryNDays\": true,\"RunNow\": true,\"RunOnce\": true,\"RunPeriodically\": false,\"StartDate\": \"2019-01-04T02:14:27.5120788-08:00\", \"WeeklyDay\": 0, \"WeeklyRecurEvery\": 0}},\"JobType\":\"CollectionJob\"}"


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"   
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
print(response.json)

