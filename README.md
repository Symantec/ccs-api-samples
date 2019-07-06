# CCS API Samples

[![Symantec](https://img.shields.io/badge/tag-symantec-yellow.svg)](https://www.symantec.com/)
[![CCS](https://img.shields.io/badge/tag-ccs-yellow.svg)](https://www.symantec.com/products/control-compliance-suite)
[![Python](https://img.shields.io/badge/language-python-blue.svg)](https://www.python.org/)
|
[![GitHub contributors](https://img.shields.io/github/contributors/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/graphs/contributors/)
|
[![GitHub issues](https://img.shields.io/github/issues/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Symantec/ccs-api-samples.svg)](https://GitHub.com/Symantec/ccs-api-samples/pull/)

**Symantec Control Compliance Suite**

Symantec Control Compliance Suite (CCS) REST API Samples

-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------

- [CCS API Samples](#CCS-API-Samples)
  - [Setup](#setup)
  - [Create Assets](#Create-Assets)
		
CreateJob.py
CreateTokens.py
DeleteAssets.py
DeleteJob.py
DeleteStandards.py
GetAllAssetsByAssetGroupID.py
SearchJobByName.py
GetAssetDetailsByID.py
SearchRemediationTickets.py
GetAssetGroupDetailsByID.py
GetEvaluationRawResults.py
GetEvaluationReport.py
UpdateRemediationTicket.py
GetLatestNJobRuns.py
GetRemediationTicketDetailsByID.py
PerformJobOperation.py
SearchAssets.py
SearchAssetsGroup.py
SearchJobByID.py
SearchStandards.py
UpdateJob.py

  - [CHANGELOG](CHANGELOG.md)
  - [License](LICENSE)

-----------------------------------------------------------------------------------------------------------------------

## Setup

Refer to Symantec CWA API documentation at: https://apidocs.symantec.com/home/CCS

-----------------------------------------------------------------------------------------------------------------------

**Code Files**

-----------------------------------------------------------------------------------------------------------------------

## Create Assets
[CreateAssets.py](CreateAssets.py)

Use this API to create an asset (What is an asset?) or multiple assets in the Control Compliance Suite asset system. This API can be used only to create assets for agentless data collection method of Control Compliance Suite.

Refer to CCS REST API at https://apidocs.symantec.com/home/CCS#_create_asset_for_agentless_data_collection_only

Usage: 
> `python CreateAssets.py -param ??`

Sample:
>  `python CreateAssets.py #`

-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------

## Change Log

See [CHANGELOG](CHANGELOG.md).

-----------------------------------------------------------------------------------------------------------------------

## License

See [License](LICENSE).